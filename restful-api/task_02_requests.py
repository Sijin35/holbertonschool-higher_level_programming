#!/usr/bin/python3
"""Consuming, proessing data from API with Python"""
import requests
import csv


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        post = r.json()
        for p in post:
            print(p["title"])

def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        post = r.json()

        new = []
        for p in post:
            new.append({
                "id": p["id"],
                "title": p["title"],
                "body": p["body"]
            })

        with open("posts.csv", "w") as csv_file:
            field = ['id', 'title', 'body']
            c = csv.DictWriter(csv_file, fieldnames=field)

            c.writeheader()
            c.writerows(new)
