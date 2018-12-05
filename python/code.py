import gc
import json
import pandas as pd

features = [
    'channelGrouping', 'date', 'fullVisitorId', 'visitId', 'visitNumber', 'visitStartTime', 'customDimensions',
    'device.browser', 'device.deviceCategory', 'device.isMobile', 'device.operatingSystem',
    'geoNetwork.city', 'geoNetwork.continent', 'geoNetwork.country', 'geoNetwork.metro', 'geoNetwork.networkDomain',
    'geoNetwork.region', 'geoNetwork.subContinent',
    'totals.bounces', 'totals.hits', 'totals.newVisits', 'totals.pageviews', 'totals.transactionRevenue',
    'trafficSource.adContent', 'trafficSource.campaign', 'trafficSource.isTrueDirect', 'trafficSource.keyword',
    'trafficSource.medium', 'trafficSource.referralPath', 'trafficSource.source'
]
