import os
import aiohttp
import asyncio

class LichessAPI:
    def __init__(self):
        self.token = os.getenv("LICHESS_BOT_TOKEN")  # Lấy token từ biến môi trường
        print(f"DEBUG: Token = {self.token}")  # Debug xem token có đúng không

    async def get_account(self):
        url = "https://lichess.org/api/account"
        headers = {"Authorization": f"Bearer {self.token}"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                json_response = await response.json()
                print(f"DEBUG: Response = {json_response}")  # Debug API response
                
                if "error" in json_response:
                    raise RuntimeError(f'Account error: {json_response["error"]}')
                
                return json_response

async def main():
    api = LichessAPI()
    account_info = await api.get_account()
    print(account_info)

if __name__ == "__main__":
    asyncio.run(main())
