# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_bluecoat_site_review"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_bluecoat_site_review package"""
    reload_params = {"package": u"fn_bluecoat_site_review",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "function_params": [u"artifact_value"], 
                    "datatables": [], 
                    "message_destinations": [u"bluecoat_site_review"], 
                    "functions": [u"bluecoat_site_review_lookup"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [u"bluecoat_site_review_search"], 
                    "actions": [u"Example: Bluecoat Site Review"] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     artifact_value
    #   Message Destinations:
    #     bluecoat_site_review
    #   Functions:
    #     bluecoat_site_review_lookup
    #   Workflows:
    #     bluecoat_site_review_search
    #   Rules:
    #     Example: Bluecoat Site Review


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbeyJ1dWlkIjogImVlOTE2NGRlLTBmN2Ut
NGZkOC1iNjVmLWUxMTBlODRjZTFjOSIsICJkZXNjcmlwdGlvbiI6ICJUaGlzIHdvcmtmbG93IGRl
bW9uc3RyYXRlcyB0aGUgQmx1ZWNvYXQgU2l0ZSBSZXZpZXcgbG9vayB1cCBmdW5jdGlvbi4gVGhl
IHJ1bGUgd29ya3Mgb24gdXJsLWJhc2VkIGFydGlmYWN0cyIsICJvYmplY3RfdHlwZSI6ICJhcnRp
ZmFjdCIsICJleHBvcnRfa2V5IjogImJsdWVjb2F0X3NpdGVfcmV2aWV3X3NlYXJjaCIsICJ3b3Jr
Zmxvd19pZCI6IDQ5LCAibGFzdF9tb2RpZmllZF9ieSI6ICJhQGV4YW1wbGUuY29tIiwgImNvbnRl
bnQiOiB7InhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48
ZGVmaW5pdGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0
L01PREVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEw
MDUyNC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1
MjQvRENcIiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0
L0RJXCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4
bWxuczp4c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1c
Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNw
YWNlPVwiaHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJibHVlY29h
dF9zaXRlX3Jldmlld19zZWFyY2hcIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFtZT1cIkV4YW1w
bGU6IEJsdWVjb2F0IFNpdGUgUmV2aWV3IFNlYXJjaFwiPjxkb2N1bWVudGF0aW9uPlRoaXMgd29y
a2Zsb3cgZGVtb25zdHJhdGVzIHRoZSBCbHVlY29hdCBTaXRlIFJldmlldyBsb29rIHVwIGZ1bmN0
aW9uLiBUaGUgcnVsZSB3b3JrcyBvbiB1cmwtYmFzZWQgYXJ0aWZhY3RzPC9kb2N1bWVudGF0aW9u
PjxzdGFydEV2ZW50IGlkPVwiU3RhcnRFdmVudF8xNTVhc3htXCI+PG91dGdvaW5nPlNlcXVlbmNl
Rmxvd18wdW54bDJ0PC9vdXRnb2luZz48L3N0YXJ0RXZlbnQ+PHNlcnZpY2VUYXNrIGlkPVwiU2Vy
dmljZVRhc2tfMWliZWZ2N1wiIG5hbWU9XCJCbHVlY29hdCBTaXRlIFJldmlldyBMb29rdXBcIiBy
ZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6
ZnVuY3Rpb24gdXVpZD1cIjJiMjY5MzJhLTYwZGYtNDA0NS1hZThkLTBlYjMxOWRlNjAxZFwiPntc
ImlucHV0c1wiOnt9LFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiIyBSZXN1bHQ6IHsnaW5w
dXRzJzoge3UnaW5jaWRlbnRfaWQnOiAyMDk5LCB1J2FydGlmYWN0X3ZhbHVlJzogdSdodHRwOi8v
bmpqaWFqaWUuY29tL3Byb2plY3QvZ2NhbC9nYW9jZW5nL2luZGV4XzMuaHRtJ30sICdtZXRyaWNz
JzogeydwYWNrYWdlJzogJ2ZuLWJsdWVjb2F0LXNpdGUtcmV2aWV3JywgJ3RpbWVzdGFtcCc6ICcy
MDE5LTAzLTI1IDE2OjU4OjA4JywgJ3BhY2thZ2VfdmVyc2lvbic6ICcxLjAuMCcsICdob3N0Jzog
J21hcmtzLW1icC5jYW1icmlkZ2UuaWJtLmNvbScsICd2ZXJzaW9uJzogJzEuMCcsICdleGVjdXRp
b25fdGltZV9tcyc6IDgwMzQ1fSwgJ3N1Y2Nlc3MnOiBUcnVlLCAnY29udGVudCc6IHt1J0NhdGVn
b3JpemF0aW9uUmVzdWx0Jzoge3UnY2F0ZWdvcml6YXRpb24nOiB7dSdjYXRlZ29yaXphdGlvbic6
IHt1J251bSc6IHUnNDMnLCB1J25hbWUnOiB1J01hbGljaW91cyBTb3VyY2VzL01hbG5ldHMnfX0s
IHUnbG9ja2VkJzogdSdmYWxzZScsIHUndHJhbnNsYXRlZENhdGVnb3JpZXMnOiB7dSdmcic6IHt1
J251bSc6IHUnNDMnLCB1J25hbWUnOiB1J1NvdXJjZXMgbWFsdmVpbGxhbnRlcy9tYWxuZXRzIChN
YWxpY2lvdXMgU291cmNlcy9NYWxuZXRzKSd9LCB1J2RlJzoge3UnbnVtJzogdSc0MycsIHUnbmFt
ZSc6IHUnQlxcXFx4ZjZzYXJ0aWdlIFF1ZWxsZW4vTWFsbmV0cyAoTWFsaWNpb3VzIFNvdXJjZXMv
TWFsbmV0cyknfSwgdSd6aCc6IHt1J251bSc6IHUnNDMnLCB1J25hbWUnOiB1J1xcXFx1NjA3Nlxc
XFx1NjEwZlxcXFx1Njc2NVxcXFx1NmU5MC9cXFxcdTYwNzZcXFxcdTYxMGZcXFxcdTdmNTFcXFxc
dTdlZGMgKE1hbGljaW91cyBTb3VyY2VzL01hbG5ldHMpJ30sIHUnemhfVFcnOiB7dSdudW0nOiB1
JzQzJywgdSduYW1lJzogdSdcXFxcdTYwZTFcXFxcdTYxMGZcXFxcdTRmODZcXFxcdTZlOTAvXFxc
XHU2MGUxXFxcXHU2MTBmXFxcXHU3ZGIyXFxcXHU4ZGVmIChNYWxpY2lvdXMgU291cmNlcy9NYWxu
ZXRzKSd9LCB1J2VuJzoge3UnbnVtJzogdSc0MycsIHUnbmFtZSc6IHUnTWFsaWNpb3VzIFNvdXJj
ZXMvTWFsbmV0cyd9LCB1J2phJzoge3UnbnVtJzogdSc0MycsIHUnbmFtZSc6IHUnXFxcXHU2MGFh
XFxcXHU2MTBmXFxcXHUzMDZlXFxcXHUzMDQyXFxcXHUzMDhiXFxcXHU3NjdhXFxcXHU0ZmUxXFxc
XHU1MTQzL1xcXFx1MzBkZVxcXFx1MzBlYlxcXFx1MzBjZFxcXFx1MzBjM1xcXFx1MzBjOCAoTWFs
aWNpb3VzIFNvdXJjZXMvTWFsbmV0cyknfSwgdSdlcyc6IHt1J251bSc6IHUnNDMnLCB1J25hbWUn
OiB1J0Z1ZW50ZXMgZGUgc29mdHdhcmUgbWFsaWNpb3NvL21hbG5ldHMgKE1hbGljaW91cyBTb3Vy
Y2VzL01hbG5ldHMpJ319LCB1J3VybCc6IHUnaHR0cDovL25qamlhamllLmNvbS9wcm9qZWN0L2dj
YWwvZ2FvY2VuZy9pbmRleF8zLmh0bScsIHUncmF0ZURhdGUnOiB1XFxcIkxhc3QgVGltZSBSYXRl
ZC9SZXZpZXdlZDogJmd0OyB7e2RheXN9fSBkYXlzIHt7bGVnYWN5fX1UaGUgVVJMIHN1Ym1pdHRl
ZCBmb3IgcmV2aWV3IHdhcyByYXRlZCBtb3JlIHRoYW4ge3tkYXlzfX0gZGF5cyBhZ28uICBUaGUg
ZGVmYXVsdCBzZXR0aW5nIGZvciBTeW1hbnRlYyBTRyBjbGllbnRzIHRvIGRvd25sb2FkIHJhdGlu
ZyBjaGFuZ2VzIGlzIG9uY2UgYSBkYXkuICBUaGVyZSBpcyBubyBuZWVkIHRvIHNob3cgcmF0aW5n
cyBvbGRlciB0aGFuIHRoaXMuIFNpbmNlIFN5bWFudGVjJ3MgZGVza3RvcCBjbGllbnQgSzkgYW5k
IGNlcnRhaW4gT0VNIHBhcnRuZXJzIHVwZGF0ZSBkaWZmZXJlbnRseSwgcmF0aW5ncyBtYXkgZGlm
ZmVyIGZyb20gdGhvc2Ugb2YgYSBTeW1hbnRlYyBTRyBhcyB3ZWxsIGFzIHRob3NlIHByZXNlbnQg
b24gdGhlIFNpdGUgUmV2aWV3IFRvb2wuXFxcIiwgdSdmb2xsb3dlZFVybCc6IE5vbmUsIHUnbG9j
a2VkU3BlY2lhbE5vdGUnOiBOb25lLCB1J3RocmVhdHJpc2tMZXZlbEVuJzogTm9uZSwgdSdsaW5r
YWJsZSc6IHUnZmFsc2UnLCB1J3Jlc29sdmVkRGV0YWlsJzoge3UncmVzb2x2ZUVuYWJsZWQnOiB1
J3RydWUnLCB1J2lwQWRkcmVzcyc6IHUnMTU0LjIxMC4yMzUuNzInfSwgdSdzZWN1cml0eUNhdGVn
b3J5SWRzJzoge3Unc2VjdXJpdHlDYXRlZ29yeUlkcyc6IFt1JzQzJywgdScxMDInLCB1JzQ0Jywg
dSc5MicsIHUnMTgnXX0sIHUnbXVsdGlwbGVNZXNzYWdlJzogTm9uZSwgdSdzdWdnZXN0aW9uJzog
Tm9uZSwgdSdzZWN1cml0eUNhdGVnb3J5JzogdSd0cnVlJywgdSdyYXRpbmdEdHNDdXRvZmYnOiB1
JzcnLCB1J211bHRpcGxlJzogdSdmYWxzZScsIHUndW5yYXRlZCc6IHUnZmFsc2UnLCB1J2N1clRy
YWNraW5nSWQnOiB1JzM5OTkyNycsIHUncmF0aW5nRHRzJzogdSdPTERFUicsIHUnbG9ja2VkTWVz
c2FnZSc6IE5vbmUsIHUndGhyZWF0cmlza0xldmVsJzogTm9uZX19LCAncmF3JzogJ3tcXFwiQ2F0
ZWdvcml6YXRpb25SZXN1bHRcXFwiOiB7XFxcImNhdGVnb3JpemF0aW9uXFxcIjoge1xcXCJjYXRl
Z29yaXphdGlvblxcXCI6IHtcXFwibnVtXFxcIjogXFxcIjQzXFxcIiwgXFxcIm5hbWVcXFwiOiBc
XFwiTWFsaWNpb3VzIFNvdXJjZXMvTWFsbmV0c1xcXCJ9fSwgXFxcImxvY2tlZFxcXCI6IFxcXCJm
YWxzZVxcXCIsIFxcXCJ0cmFuc2xhdGVkQ2F0ZWdvcmllc1xcXCI6IHtcXFwiZnJcXFwiOiB7XFxc
Im51bVxcXCI6IFxcXCI0M1xcXCIsIFxcXCJuYW1lXFxcIjogXFxcIlNvdXJjZXMgbWFsdmVpbGxh
bnRlcy9tYWxuZXRzIChNYWxpY2lvdXMgU291cmNlcy9NYWxuZXRzKVxcXCJ9LCBcXFwiZGVcXFwi
OiB7XFxcIm51bVxcXCI6IFxcXCI0M1xcXCIsIFxcXCJuYW1lXFxcIjogXFxcIkJcXFxcXFxcXHUw
MGY2c2FydGlnZSBRdWVsbGVuL01hbG5ldHMgKE1hbGljaW91cyBTb3VyY2VzL01hbG5ldHMpXFxc
In0sIFxcXCJ6aFxcXCI6IHtcXFwibnVtXFxcIjogXFxcIjQzXFxcIiwgXFxcIm5hbWVcXFwiOiBc
XFwiXFxcXFxcXFx1NjA3NlxcXFxcXFxcdTYxMGZcXFxcXFxcXHU2NzY1XFxcXFxcXFx1NmU5MC9c
XFxcXFxcXHU2MDc2XFxcXFxcXFx1NjEwZlxcXFxcXFxcdTdmNTFcXFxcXFxcXHU3ZWRjIChNYWxp
Y2lvdXMgU291cmNlcy9NYWxuZXRzKVxcXCJ9LCBcXFwiemhfVFdcXFwiOiB7XFxcIm51bVxcXCI6
IFxcXCI0M1xcXCIsIFxcXCJuYW1lXFxcIjogXFxcIlxcXFxcXFxcdTYwZTFcXFxcXFxcXHU2MTBm
XFxcXFxcXFx1NGY4NlxcXFxcXFxcdTZlOTAvXFxcXFxcXFx1NjBlMVxcXFxcXFxcdTYxMGZcXFxc
XFxcXHU3ZGIyXFxcXFxcXFx1OGRlZiAoTWFsaWNpb3VzIFNvdXJjZXMvTWFsbmV0cylcXFwifSwg
XFxcImVuXFxcIjoge1xcXCJudW1cXFwiOiBcXFwiNDNcXFwiLCBcXFwibmFtZVxcXCI6IFxcXCJN
YWxpY2lvdXMgU291cmNlcy9NYWxuZXRzXFxcIn0sIFxcXCJqYVxcXCI6IHtcXFwibnVtXFxcIjog
XFxcIjQzXFxcIiwgXFxcIm5hbWVcXFwiOiBcXFwiXFxcXFxcXFx1NjBhYVxcXFxcXFxcdTYxMGZc
XFxcXFxcXHUzMDZlXFxcXFxcXFx1MzA0MlxcXFxcXFxcdTMwOGJcXFxcXFxcXHU3NjdhXFxcXFxc
XFx1NGZlMVxcXFxcXFxcdTUxNDMvXFxcXFxcXFx1MzBkZVxcXFxcXFxcdTMwZWJcXFxcXFxcXHUz
MGNkXFxcXFxcXFx1MzBjM1xcXFxcXFxcdTMwYzggKE1hbGljaW91cyBTb3VyY2VzL01hbG5ldHMp
XFxcIn0sIFxcXCJlc1xcXCI6IHtcXFwibnVtXFxcIjogXFxcIjQzXFxcIiwgXFxcIm5hbWVcXFwi
OiBcXFwiRnVlbnRlcyBkZSBzb2Z0d2FyZSBtYWxpY2lvc28vbWFsbmV0cyAoTWFsaWNpb3VzIFNv
dXJjZXMvTWFsbmV0cylcXFwifX0sIFxcXCJ1cmxcXFwiOiBcXFwiaHR0cDovL25qamlhamllLmNv
bS9wcm9qZWN0L2djYWwvZ2FvY2VuZy9pbmRleF8zLmh0bVxcXCIsIFxcXCJyYXRlRGF0ZVxcXCI6
IFxcXCJMYXN0IFRpbWUgUmF0ZWQvUmV2aWV3ZWQ6ICZndDsge3tkYXlzfX0gZGF5cyB7e2xlZ2Fj
eX19VGhlIFVSTCBzdWJtaXR0ZWQgZm9yIHJldmlldyB3YXMgcmF0ZWQgbW9yZSB0aGFuIHt7ZGF5
c319IGRheXMgYWdvLiAgVGhlIGRlZmF1bHQgc2V0dGluZyBmb3IgU3ltYW50ZWMgU0cgY2xpZW50
cyB0byBkb3dubG9hZCByYXRpbmcgY2hhbmdlcyBpcyBvbmNlIGEgZGF5LiAgVGhlcmUgaXMgbm8g
bmVlZCB0byBzaG93IHJhdGluZ3Mgb2xkZXIgdGhhbiB0aGlzLiBTaW5jZSBTeW1hbnRlY1xcXFwn
cyBkZXNrdG9wIGNsaWVudCBLOSBhbmQgY2VydGFpbiBPRU0gcGFydG5lcnMgdXBkYXRlIGRpZmZl
cmVudGx5LCByYXRpbmdzIG1heSBkaWZmZXIgZnJvbSB0aG9zZSBvZiBhIFN5bWFudGVjIFNHIGFz
IHdlbGwgYXMgdGhvc2UgcHJlc2VudCBvbiB0aGUgU2l0ZSBSZXZpZXcgVG9vbC5cXFwiLCBcXFwi
Zm9sbG93ZWRVcmxcXFwiOiBudWxsLCBcXFwibG9ja2VkU3BlY2lhbE5vdGVcXFwiOiBudWxsLCBc
XFwidGhyZWF0cmlza0xldmVsRW5cXFwiOiBudWxsLCBcXFwibGlua2FibGVcXFwiOiBcXFwiZmFs
c2VcXFwiLCBcXFwicmVzb2x2ZWREZXRhaWxcXFwiOiB7XFxcInJlc29sdmVFbmFibGVkXFxcIjog
XFxcInRydWVcXFwiLCBcXFwiaXBBZGRyZXNzXFxcIjogXFxcIjE1NC4yMTAuMjM1LjcyXFxcIn0s
IFxcXCJzZWN1cml0eUNhdGVnb3J5SWRzXFxcIjoge1xcXCJzZWN1cml0eUNhdGVnb3J5SWRzXFxc
IjogW1xcXCI0M1xcXCIsIFxcXCIxMDJcXFwiLCBcXFwiNDRcXFwiLCBcXFwiOTJcXFwiLCBcXFwi
MThcXFwiXX0sIFxcXCJtdWx0aXBsZU1lc3NhZ2VcXFwiOiBudWxsLCBcXFwic3VnZ2VzdGlvblxc
XCI6IG51bGwsIFxcXCJzZWN1cml0eUNhdGVnb3J5XFxcIjogXFxcInRydWVcXFwiLCBcXFwicmF0
aW5nRHRzQ3V0b2ZmXFxcIjogXFxcIjdcXFwiLCBcXFwibXVsdGlwbGVcXFwiOiBcXFwiZmFsc2Vc
XFwiLCBcXFwidW5yYXRlZFxcXCI6IFxcXCJmYWxzZVxcXCIsIFxcXCJjdXJUcmFja2luZ0lkXFxc
IjogXFxcIjM5OTkyN1xcXCIsIFxcXCJyYXRpbmdEdHNcXFwiOiBcXFwiT0xERVJcXFwiLCBcXFwi
bG9ja2VkTWVzc2FnZVxcXCI6IG51bGwsIFxcXCJ0aHJlYXRyaXNrTGV2ZWxcXFwiOiBudWxsfX0n
LCAncmVhc29uJzogTm9uZSwgJ3ZlcnNpb24nOiAnMS4wJ31cXG5pZiBpc2luc3RhbmNlKHJlc3Vs
dHMuY29udGVudFsnQ2F0ZWdvcml6YXRpb25SZXN1bHQnXVsnY2F0ZWdvcml6YXRpb24nXVsnY2F0
ZWdvcml6YXRpb24nXSxsaXN0KTpcXG4gIGNhdGVnb3JpemF0aW9uX2xpc3QgPSBbY2F0ZWdvcml6
YXRpb25bJ25hbWUnXSBmb3IgY2F0ZWdvcml6YXRpb24gaW4gcmVzdWx0cy5jb250ZW50WydDYXRl
Z29yaXphdGlvblJlc3VsdCddWydjYXRlZ29yaXphdGlvbiddWydjYXRlZ29yaXphdGlvbiddXVxc
biAgY2F0ZWdvcml6YXRpb25fbmFtZSA9IHVcXFwiLCBcXFwiLmpvaW4oY2F0ZWdvcml6YXRpb25f
bGlzdClcXG5lbHNlOlxcbiAgY2F0ZWdvcml6YXRpb25fbmFtZSA9IHJlc3VsdHMuY29udGVudFsn
Q2F0ZWdvcml6YXRpb25SZXN1bHQnXVsnY2F0ZWdvcml6YXRpb24nXVsnY2F0ZWdvcml6YXRpb24n
XVsnbmFtZSddXFxuICBcXG5leGlzdGluZ19kZXNjcmlwdGlvbiA9IGFydGlmYWN0LmRlc2NyaXB0
aW9uLmNvbnRlbnQrJ1xcXFxuJyBpZiBhcnRpZmFjdC5kZXNjcmlwdGlvbiBlbHNlIFxcXCJcXFwi
XFxuXFxuYXJ0aWZhY3QuZGVzY3JpcHRpb24gPSB1XFxcInt9Qmx1ZWNvYXQgQ2F0ZWdvcml6YXRp
b246IHt9XFxcIi5mb3JtYXQoZXhpc3RpbmdfZGVzY3JpcHRpb24sIGNhdGVnb3JpemF0aW9uX25h
bWUpXFxuICBcXG5cXG5cIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiaW5wdXRzLmFydGlm
YWN0X3ZhbHVlID0gYXJ0aWZhY3QudmFsdWVcXG5cIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4
dGVuc2lvbkVsZW1lbnRzPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMHVueGwydDwvaW5jb21pbmc+
PG91dGdvaW5nPlNlcXVlbmNlRmxvd18xZ3JzY290PC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxz
ZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMHVueGwydFwiIHNvdXJjZVJlZj1cIlN0YXJ0
RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNrXzFpYmVmdjdcIi8+PGVuZEV2
ZW50IGlkPVwiRW5kRXZlbnRfMDdxajl4M1wiPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMWdyc2Nv
dDwvaW5jb21pbmc+PC9lbmRFdmVudD48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzFn
cnNjb3RcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18xaWJlZnY3XCIgdGFyZ2V0UmVmPVwiRW5k
RXZlbnRfMDdxajl4M1wiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4
aXl0XCI+PHRleHQ+U3RhcnQgeW91ciB3b3JrZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRp
b24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0
YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+
PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMWpod2JjaFwiPjx0ZXh0PlJlc3Vs
dHMgYXJlIGFwcGVuZGVkIHRvIHRoZSBhcnRpZmFjdCBkZXNjcmlwdGlvbjwvdGV4dD48L3RleHRB
bm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzB6MzgzZWpcIiBzb3VyY2VS
ZWY9XCJTZXJ2aWNlVGFza18xaWJlZnY3XCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25fMWpo
d2JjaFwiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBpZD1cIkJQTU5EaWFncmFtXzFc
Ij48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVudD1cInVuZGVmaW5lZFwiIGlkPVwiQlBNTlBs
YW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlN0YXJ0RXZlbnRfMTU1YXN4
bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIz
NlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYyXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48
b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1cIjkwXCIgeD1cIjE1N1wiIHk9XCIyMjNc
Ii8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFw
ZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIiBpZD1cIlRleHRBbm5vdGF0
aW9uXzFreHhpeXRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjMwXCIgd2lkdGg9XCIxMDBc
IiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdl
IGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIGlkPVwiQXNzb2NpYXRpb25fMXNl
dWo0OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTY5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2lu
dFwiIHk9XCIyMjBcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIxNTNcIiB4c2k6dHlwZT1cIm9tZ2Rj
OlBvaW50XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBi
cG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzFpYmVmdjdcIiBpZD1cIlNlcnZpY2VUYXNrXzFpYmVm
djdfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwiMjc4
XCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxl
bWVudD1cIlNlcXVlbmNlRmxvd18wdW54bDJ0XCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMHVueGwydF9k
aVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9
XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIyNzhcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50
XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEz
XCIgd2lkdGg9XCI5MFwiIHg9XCIxOTNcIiB5PVwiMTg0LjVcIi8+PC9icG1uZGk6QlBNTkxhYmVs
PjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiRW5kRXZl
bnRfMDdxajl4M1wiIGlkPVwiRW5kRXZlbnRfMDdxajl4M19kaVwiPjxvbWdkYzpCb3VuZHMgaGVp
Z2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjQ1NVwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1O
TGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiOTBcIiB4PVwiNDI4XCIg
eT1cIjIyN1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6
QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMWdyc2NvdFwiIGlkPVwiU2VxdWVu
Y2VGbG93XzFncnNjb3RfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjM3OFwiIHhzaTp0eXBlPVwi
b21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNDU1XCIgeHNpOnR5
cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJv
dW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiOTBcIiB4PVwiMzcxLjVcIiB5PVwiMTg0LjVcIi8+
PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJw
bW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25fMWpod2JjaFwiIGlkPVwiVGV4dEFubm90YXRpb25f
MWpod2JjaF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiNDNcIiB3aWR0aD1cIjE0OFwiIHg9
XCIzNzFcIiB5PVwiODBcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBt
bkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8wejM4M2VqXCIgaWQ9XCJBc3NvY2lhdGlvbl8wejM4M2Vq
X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIzNzBcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIg
eT1cIjE2OFwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjQyMVwiIHhzaTp0eXBlPVwib21nZGM6UG9p
bnRcIiB5PVwiMTIzXCIvPjwvYnBtbmRpOkJQTU5FZGdlPjwvYnBtbmRpOkJQTU5QbGFuZT48L2Jw
bW5kaTpCUE1ORGlhZ3JhbT48L2RlZmluaXRpb25zPiIsICJ3b3JrZmxvd19pZCI6ICJibHVlY29h
dF9zaXRlX3Jldmlld19zZWFyY2giLCAidmVyc2lvbiI6IDEwfSwgImxhc3RfbW9kaWZpZWRfdGlt
ZSI6IDE1NTM1NTY5OTM2NzEsICJjcmVhdG9yX2lkIjogImFAZXhhbXBsZS5jb20iLCAiYWN0aW9u
cyI6IFtdLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiYmx1ZWNvYXRfc2l0ZV9yZXZpZXdfc2VhcmNo
IiwgIm5hbWUiOiAiRXhhbXBsZTogQmx1ZWNvYXQgU2l0ZSBSZXZpZXcgU2VhcmNoIn1dLCAiYWN0
aW9ucyI6IFt7ImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm5hbWUiOiAiRXhhbXBsZTogQmx1ZWNvYXQg
U2l0ZSBSZXZpZXciLCAidmlld19pdGVtcyI6IFtdLCAidHlwZSI6IDEsICJ3b3JrZmxvd3MiOiBb
ImJsdWVjb2F0X3NpdGVfcmV2aWV3X3NlYXJjaCJdLCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZhY3Qi
LCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ1dWlkIjogIjNiYTA4Y2VjLWY1NzMtNDg5Ny05
YzEyLTMwOTNiMTVhNGUzMSIsICJhdXRvbWF0aW9ucyI6IFtdLCAiZXhwb3J0X2tleSI6ICJFeGFt
cGxlOiBCbHVlY29hdCBTaXRlIFJldmlldyIsICJjb25kaXRpb25zIjogW3sidHlwZSI6IG51bGws
ICJldmFsdWF0aW9uX2lkIjogbnVsbCwgImZpZWxkX25hbWUiOiAiYXJ0aWZhY3QudHlwZSIsICJt
ZXRob2QiOiAiaW4iLCAidmFsdWUiOiBbIkROUyBOYW1lIiwgIlVSTCJdfV0sICJpZCI6IDY5LCAi
bWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbXX1dLCAibGF5b3V0cyI6IFtdLCAiZXhwb3J0X2Zvcm1h
dF92ZXJzaW9uIjogMiwgImlkIjogMjEsICJpbmR1c3RyaWVzIjogbnVsbCwgInBoYXNlcyI6IFtd
LCAiYWN0aW9uX29yZGVyIjogW10sICJnZW9zIjogbnVsbCwgImxvY2FsZSI6IG51bGwsICJzZXJ2
ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMSwgInZlcnNpb24iOiAiMzEuMC40MjU0IiwgImJ1aWxk
X251bWJlciI6IDQyNTQsICJtaW5vciI6IDB9LCAidGltZWZyYW1lcyI6IG51bGwsICJ3b3Jrc3Bh
Y2VzIjogW10sICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgImZ1bmN0aW9ucyI6IFt7ImRpc3BsYXlf
bmFtZSI6ICJCbHVlY29hdCBTaXRlIFJldmlldyBMb29rdXAiLCAiZGVzY3JpcHRpb24iOiB7ImNv
bnRlbnQiOiAiVGhpcyBmdW5jdGlvbiB0YWtlcyBhbiBhcnRpZmFjdCBvZiB0eXBlIFVSTCBvciBE
TlMgbmFtZSBhbmQgcmV0dXJucyB0aG9zZSByZXN1bHRzIGFzIGEganNvbiBvYmplY3QuIiwgImZv
cm1hdCI6ICJ0ZXh0In0sICJjcmVhdG9yIjogeyJkaXNwbGF5X25hbWUiOiAiYWJsZSBiYWNrZXIi
LCAidHlwZSI6ICJ1c2VyIiwgImlkIjogMywgIm5hbWUiOiAiYUBleGFtcGxlLmNvbSJ9LCAidmll
d19pdGVtcyI6IFt7InNob3dfaWYiOiBudWxsLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwg
InNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJjb250
ZW50IjogIjliYTQ5ODg3LTBkY2YtNDBjZS1hNWVhLTljMGM0M2Y4MzFiZiIsICJzdGVwX2xhYmVs
IjogbnVsbH1dLCAiZXhwb3J0X2tleSI6ICJibHVlY29hdF9zaXRlX3Jldmlld19sb29rdXAiLCAi
dXVpZCI6ICIyYjI2OTMyYS02MGRmLTQwNDUtYWU4ZC0wZWIzMTlkZTYwMWQiLCAibGFzdF9tb2Rp
ZmllZF9ieSI6IHsiZGlzcGxheV9uYW1lIjogImFibGUgYmFja2VyIiwgInR5cGUiOiAidXNlciIs
ICJpZCI6IDMsICJuYW1lIjogImFAZXhhbXBsZS5jb20ifSwgInZlcnNpb24iOiAyLCAid29ya2Zs
b3dzIjogW3siZGVzY3JpcHRpb24iOiBudWxsLCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZhY3QiLCAi
YWN0aW9ucyI6IFtdLCAibmFtZSI6ICJFeGFtcGxlOiBCbHVlY29hdCBTaXRlIFJldmlldyBTZWFy
Y2giLCAid29ya2Zsb3dfaWQiOiA0OSwgInByb2dyYW1tYXRpY19uYW1lIjogImJsdWVjb2F0X3Np
dGVfcmV2aWV3X3NlYXJjaCIsICJ1dWlkIjogbnVsbH1dLCAibGFzdF9tb2RpZmllZF90aW1lIjog
MTU1MzU1Njk3NjM2NCwgImRlc3RpbmF0aW9uX2hhbmRsZSI6ICJibHVlY29hdF9zaXRlX3Jldmll
dyIsICJpZCI6IDM3LCAibmFtZSI6ICJibHVlY29hdF9zaXRlX3Jldmlld19sb29rdXAifV0sICJu
b3RpZmljYXRpb25zIjogbnVsbCwgInJlZ3VsYXRvcnMiOiBudWxsLCAiaW5jaWRlbnRfdHlwZXMi
OiBbeyJjcmVhdGVfZGF0ZSI6IDE1NTM1NTk0NDcxNzEsICJkZXNjcmlwdGlvbiI6ICJDdXN0b21p
emF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZXhwb3J0X2tleSI6ICJDdXN0b21pemF0aW9u
IFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiaWQiOiAwLCAibmFtZSI6ICJDdXN0b21pemF0aW9uIFBh
Y2thZ2VzIChpbnRlcm5hbCkiLCAidXBkYXRlX2RhdGUiOiAxNTUzNTU5NDQ3MTcxLCAidXVpZCI6
ICJiZmVlYzJkNC0zNzcwLTExZTgtYWQzOS00YTAwMDQwNDRhYTAiLCAiZW5hYmxlZCI6IGZhbHNl
LCAic3lzdGVtIjogZmFsc2UsICJwYXJlbnRfaWQiOiBudWxsLCAiaGlkZGVuIjogZmFsc2V9XSwg
InNjcmlwdHMiOiBbXSwgInR5cGVzIjogW10sICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFt7InV1
aWQiOiAiYzg5YmNlNmQtMDFmOC00N2U3LThkNGMtNWQ3OTNiMWVhNmI2IiwgImV4cG9ydF9rZXki
OiAiYmx1ZWNvYXRfc2l0ZV9yZXZpZXciLCAibmFtZSI6ICJCbHVlY29hdCBTaXRlIFJldmlldyIs
ICJkZXN0aW5hdGlvbl90eXBlIjogMCwgInByb2dyYW1tYXRpY19uYW1lIjogImJsdWVjb2F0X3Np
dGVfcmV2aWV3IiwgImV4cGVjdF9hY2siOiB0cnVlLCAidXNlcnMiOiBbImFAZXhhbXBsZS5jb20i
XX1dLCAiaW5jaWRlbnRfYXJ0aWZhY3RfdHlwZXMiOiBbXSwgInJvbGVzIjogW10sICJmaWVsZHMi
OiBbeyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMCwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9
LCAidGV4dCI6ICJTaW11bGF0aW9uIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4Ijog
bnVsbCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiA1MSwgInJlYWRfb25seSI6IHRydWUsICJ1
dWlkIjogImMzZjBlM2VkLTIxZTEtNGQ1My1hZmZiLWZlNWNhMzMwOGNjYSIsICJjaG9zZW4iOiBm
YWxzZSwgImlucHV0X3R5cGUiOiAiYm9vbGVhbiIsICJ0b29sdGlwIjogIldoZXRoZXIgdGhlIGlu
Y2lkZW50IGlzIGEgc2ltdWxhdGlvbiBvciBhIHJlZ3VsYXIgaW5jaWRlbnQuICBUaGlzIGZpZWxk
IGlzIHJlYWQtb25seS4iLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAi
dGVtcGxhdGVzIjogW10sICJleHBvcnRfa2V5IjogImluY2lkZW50L2luY190cmFpbmluZyIsICJo
aWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAibmFtZSI6ICJpbmNfdHJhaW5pbmciLCAiZGVwcmVj
YXRlZCI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJ2YWx1ZXMi
OiBbXX0sIHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDExLCAib3BlcmF0aW9uX3Blcm1z
Ijoge30sICJ0ZXh0IjogImFydGlmYWN0X3ZhbHVlIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAi
cHJlZml4IjogbnVsbCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAyODUsICJyZWFkX29ubHki
OiBmYWxzZSwgInV1aWQiOiAiOWJhNDk4ODctMGRjZi00MGNlLWE1ZWEtOWMwYzQzZjgzMWJmIiwg
ImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAiIiwgImlu
dGVybmFsIjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhw
b3J0X2tleSI6ICJfX2Z1bmN0aW9uL2FydGlmYWN0X3ZhbHVlIiwgImhpZGVfbm90aWZpY2F0aW9u
IjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJhcnRpZmFjdF92YWx1ZSIsICJk
ZXByZWNhdGVkIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZh
bHVlcyI6IFtdfV0sICJvdmVycmlkZXMiOiBbXSwgImV4cG9ydF9kYXRlIjogMTU1MzU1OTQzMzAy
Nn0=
"""
    )