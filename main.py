import random
import genanki
from datetime import datetime

def create_anki_card(content):
    front = content[:20]
    # 随机挖空前20个字符中的5个字符
    for _ in range(5):
        idx = random.randint(0, len(front) - 1)
        front = front[:idx] + '_' + front[idx + 1:]
    back = content
    return (front, back)

# 从memo.txt中读取文本
with open('memo.txt', 'r', encoding='utf-8') as file:
    raw_content = file.read()

contents = raw_content.split('$$$')
contents = [content.strip() for content in contents if content.strip()]

# 创建Anki卡片
cards = []
for content in contents:
    front, back = create_anki_card(content)
    cards.append((front, back))

# 创建Anki牌组
model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '<div style="font-size: 30px; font-family: PingFang SC, sans-serif; text-align: center;">{{Question}}</div>',
      'afmt': '{{FrontSide}}<hr id="answer"><div style="font-size: 20px; line-height: 1.6; font-family: PingFang SC, sans-serif; text-align: left; width: 80%; margin: 0 auto; padding: 20px; background-color: #f9f9f9; border-radius: 10px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">{{Answer}}</div>',
    },
  ])

# 获取当前时间
current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

deck = genanki.Deck(
  2059400110,
  f'{current_time} Desk')

for front, back in cards:
    note = genanki.Note(model=model, fields=[front, back])
    deck.add_note(note)

# 将牌组导出为.apkg文件
output_filename = f'{current_time}.apkg'
genanki.Package(deck).write_to_file(output_filename)