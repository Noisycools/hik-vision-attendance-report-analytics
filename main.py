from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from mysql.connector import connect, Error
from sqlalchemy import create_engine
from dotenv import load_dotenv
import time
import pandas as pd
import os
import glob

load_dotenv()

DATABASE_NAME = os.getenv("DB_NAME")
TABLE_NAME = "attendance_summary"

EXCEL_FILE_PATH = os.getenv("EXCEL_FILE_PATH")


def get_latest_file(folder_path):
    list_of_files = glob.glob(os.path.join(folder_path, "*"))

    if not list_of_files:
        print("No files found in the folder.")
        return None

    latest_file = max(list_of_files, key=os.path.getmtime)

    return latest_file


def extractExcelData(filename):
    file_path = "files/{0}".format(filename)
    df = pd.read_excel(file_path, skiprows=4, header=[0, 1])
    df.columns = [" ".join(col).strip() for col in df.columns.values]
    df.columns = [
        col if "Unnamed" not in col else col.split(" ")[0] for col in df.columns
    ]
    # print(df.columns)

    df.rename(
        columns={
            "Employee": "employee_id",
            "Name": "name",
            "Department": "department",
            "Work Duration Standard": "work_duration_standard",
            "Work Duration Actual": "work_duration_actual",
            "Late Times": "late_times",
            "Late Duration(min)": "late_duration_min",
            "Leave Early Times": "leave_early_times",
            "Leave Early Duration(min)": "leave_early_duration_min",
            "OverTime Normal": "overtime_normal",
            "OverTime Special": "overtime_special",
            "Lack Times": "lack_times",
            "Lack Duration(min)": "lack_duration_min",
            "Attendance": "attendance",
            "Absent(Days)": "absent_days",
            "On": "on_business_days",
            "Ask": "ask_off",
            "Salary Raise Mark": "salary_raise_mark",
            "Salary Raise Over Time": "salary_raise_over_time",
            "Salary Raise Subsidy": "salary_raise_subsidy",
            "Salary reduce Late/Leave early": "salary_reduce_late_leave_early",
            "Salary reduce Casual Leave": "salary_reduce_casual_leave",
            "Salary reduce Chargeback": "salary_reduce_chargeback",
            "Real": "real_wage",
            "Remarks": "remarks",
        },
        inplace=True,
    )

    # df_selected = df[columns_of_interest]

    # print(df.head())

    # Initialize db engine
    engine = create_engine(
        "mysql+pymysql://{}:{}@localhost:3306/{}".format(
            os.getenv("DB_USERNAME"), os.getenv("DB_PASSWORD"), os.getenv("DB_NAME")
        )
    )

    df.to_sql("attendance_summary", con=engine, if_exists="replace", index=False)

    try:
        with connect(
            host="localhost",
            user=os.getenv("DB_USERNAME"),
            password=os.getenv("DB_PASSWORD"),
            database=DATABASE_NAME,
        ) as connection:
            print("Database connection established")

            set_primary_key_employee_id_query = """
            ALTER TABLE attendance_summary
            ADD PRIMARY KEY (employee_id);
            """

            with connection.cursor() as cursor:
                cursor.execute(set_primary_key_employee_id_query)
                connection.commit()
    except Error as e:
        print(e)


def downloadReport():
    options = Options()
    options.enable_downloads = True
    options.accept_insecure_certs = True
    prefs = {"download.default_directory": r"{}".format(EXCEL_FILE_PATH)}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)

    driver.get("https://192.0.0.64/doc/index.html#/portal/login")

    try:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[placeholder='User Name']")
            )
        )

        driver.find_element(
            by=By.CSS_SELECTOR,
            value="input[placeholder='User Name']",
        ).send_keys("admin")
        driver.find_element(
            by=By.CSS_SELECTOR, value="input[type='password']"
        ).send_keys("sccic2024")

        driver.find_element(by=By.CLASS_NAME, value="login-btn").click()

        time.sleep(2)

        driver.get("https://192.0.0.64/doc/index.html#/attendanceReport/reportSummary")

        time.sleep(2)

        driver.find_element(by=By.CLASS_NAME, value="export").click()

        time.sleep(5)

        # html = driver.page_source
        # soup = BeautifulSoup(html, "html.parser")
        # print(len(soup.select("li.el-tooltip")))
    except:
        print("An error occurred")

    driver.quit()


def main():
    downloadReport()

    latest_file = get_latest_file("files/")
    if latest_file:
        extractExcelData(os.path.basename(latest_file))


if __name__ == "__main__":
    main()
