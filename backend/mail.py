import smtplib

smtp_host = 'localhost'
smtp_port = 1025

from_addr = '22f3002857@ds.study.iitm.ac.in'


def send_daily_reminder(to_addr):
    subject = 'Make sure to check our application'
    body = 'Hey user, this is a reminder to check our application for any updates or tasks that need your attention.'

    message = f"""From: {from_addr}\nTo: {to_addr}\nSubject: {subject}\n\n{body}"""

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.sendmail(from_addr, to_addr, message)


def send_monthly_reminder(to_addr, data=None):
    # use data to generate the body and send to user
    subject = 'Here is your previos month report'
    body = 'Hey user, thanks for using our application. This is your monthly activity report.\nYour booking in this month\n' + 'Day1: Reliance slot2\nDay2: Reliance slot2\nDay3: Reliance slot2\nDay4: Reliance slot2\nDay5: Reliance slot2\nDay6: Reliance slot2\nDay7: Reliance slot2\nDay8: Reliance slot2\nDay9: Reliance slot2\nDay10: Reliance slot2\nDay11: Reliance slot2\nDay12: Reliance slot2\nDay13: Reliance slot2\nDay14: Reliance slot2\nDay15: Reliance slot2\nDay16: Reliance slot2\nDay17: Reliance slot2\nDay18: Reliance slot2\nDay19: Reliance slot2\nDay20: Reliance slot2'

    message = f"""From: {from_addr}\nTo: {to_addr}\nSubject: {subject}\n\n{body}"""

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.sendmail(from_addr, to_addr, message)
    

import csv
import os

def save_to_csv(data, filepath):
    if not data:
        raise ValueError("Data is empty. Nothing to write.")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    fieldnames = data[0].keys()
    with open(filepath, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"✅ CSV saved to: {filepath}")

def send_export_job_result(to_addr, data=None):
    # user = User.query.filter_by(email='admin@gmail.com').first()
    # get the data of user to export to csv
    save_to_csv(
        data = [
            {"name": "Alice", "age": 30, "city": "NY"},
            {"name": "Bob", "age": 25, "city": "LA"},
            {"name": "Charlie", "age": 35, "city": "Chicago"}
        ],
        filepath=os.path.join('static', 'csv_exports', f'{to_addr}.csv')
    )
    link = 'http://localhost:5000/static/csv_exports/' + f'{to_addr}.csv'

    subject = 'Here is your csv export'
    body = 'Hey user, click this link to download your csv file\n' + link

    message = f"""From: {from_addr}\nTo: {to_addr}\nSubject: {subject}\n\n{body}"""

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.sendmail(from_addr, to_addr, message)
    
    print("Export job result sent successfully.")
