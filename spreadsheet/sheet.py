import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]

json_file_name = 'google_auth.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    json_file_name, scope)

gc = gspread.authorize(credentials)

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/12-c1GsrezczRSRNNNI_FerE1oSeEE4kUw5eXI_cw4Oo/edit#gid=0'
# 스프레스시트 문서 가져오기
doc = gc.open_by_url(spreadsheet_url)

# 시트 선택하기
worksheet = doc.worksheet('lucky')

# 행운 봇 중 뽑기
def LuckyDraw():
    luckyContent = worksheet.col_values(2)
    result = random.choice(luckyContent)
    return result

print('랜덤뽑기 중 . . . ')
print(LuckyDraw())