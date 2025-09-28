import discord
import os

intents = discord.Intents.default()
intents.message_content = True  # cần bật để bot đọc nội dung tin nhắn

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot đã đăng nhập với tên: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.strip() == "!go":
        await message.channel.send("✅ Bắt đầu gửi biểu đồ")
        for stick in ["AAA", "BBB", "CCC"]:
            await message.channel.send(f"Đang xử lý mã: {stick}")

# Khởi động bot
client.run(os.getenv("DISCORD_TOKEN"))
