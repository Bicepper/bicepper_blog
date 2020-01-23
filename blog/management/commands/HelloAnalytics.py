"""Hello Analytics Reporting API V4."""
import argparse
import os

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_FILE_LOCATION = os.path.join(BASE_DIR, 'Bicepperblog-e1b896d8062e.p12')
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
DISCOVERY_URI = ('https://analyticsreporting.googleapis.com/$discovery/rest')

SERVICE_ACCOUNT_EMAIL = 'bicepper-blog-pv-read@bicepperblog.iam.gserviceaccount.com'
VIEW_ID = '197751694'


def initialize_analyticsreporting():
    """Initializes an analyticsreporting service object.

    Returns:   analytics an authorized analyticsreporting service
    object.

    """

    credentials = ServiceAccountCredentials.from_p12_keyfile(
        SERVICE_ACCOUNT_EMAIL, KEY_FILE_LOCATION, scopes=SCOPES)

    http = credentials.authorize(httplib2.Http())

    # Build the service object.
    analytics = build('analytics', 'v4', http=http,
                      discoveryServiceUrl=DISCOVERY_URI)

    return analytics


def get_report(analytics):
    # Use the Analytics Service Object to query the Analytics Reporting API V4.
    return analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': VIEW_ID,
                    'pageSize': 3,
                    'filtersExpression': 'ga:pagePath=@detail;ga:pageTitle!@404',
                    'dateRanges': [
                        {'startDate': '7daysAgo', 'endDate': 'today'}
                    ],
                    'metrics': [
                        {'expression': 'ga:pageviews'},
                    ],
                    'dimensions': [
                        {'name': 'ga:pagePath'}, {'name': 'ga:pageTitle'}
                    ],
                    'orderBys': [
                        {'fieldName': 'ga:pageviews', 'sortOrder': 'DESCENDING'},
                    ]
                }]
        }
    ).execute()


def get_10_popular():
    """過去1週間の人気ページを10件返す

    URL、ページタイトル、PV数をyieldで返します

    """
    analytics = initialize_analyticsreporting()
    response = get_report(analytics)
    for report in response.get('reports', []):
        rows = report.get('data', {}).get('rows', [])
        for row in rows:
            url = row['dimensions'][0]
            page_view = row['metrics'][0]['values'][0]
            yield url, int(page_view)


if __name__ == '__main__':
    for url, page_view in get_10_popular():
        print(url, page_view)