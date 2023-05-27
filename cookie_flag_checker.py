import aiohttp
import asyncio

session_ids = ['ASP.NET_SessionId', 'PHPSESSID', 'JSESSIONID'] # Update the session_ids if needed
request_timeout = 20  # Timeout value in seconds

async def check_cookie_flags(session_id, url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=request_timeout) as response:
                cookies = response.cookies

                if session_id in cookies:
                    cookie = cookies[session_id]
                    secure = cookie.get('secure')
                    httponly = cookie.get('httponly')

                    if secure is not True:
                        secure = '---missing'

                    if httponly is not True:
                        httponly = '---missing'

                    return secure, httponly

                return None, None
    except aiohttp.InvalidURL as e:
        print(f"Invalid URL: {e}")
        return None, None
    except aiohttp.ClientConnectorError as e:
        print(f"Connection error: {e}")
        return None, None
    except asyncio.TimeoutError as e:
        print(f"Timeout error: {e}")
        return None, None
    except aiohttp.ServerDisconnectedError as e:
        print(f"Server disconnected error: {e}")
        return None, None

file_path = 'url_list.txt'  # Replace with the path to your text file
with open(file_path, 'r') as file:
    urls = file.read().splitlines()

async def check_domains():
    for url in urls:
        print(f"Checking URL: {url}")
        for session_id in session_ids:
            try:
                secure, httponly = await check_cookie_flags(session_id, url)
                if secure is not None and httponly is not None:
                    print(f"Domain: {url}")
                    print(f"Session ID: {session_id}")
                    print(f"Secure: {secure}")
                    print(f"HttpOnly: {httponly}")
                    print("====================")
                    break  # Skip checking other session IDs for this URL
            except Exception as e:
                print(f"An error occurred: {e}")
                break  # Skip the current URL if an error occurs
        print("")
        print("")

asyncio.run(check_domains())
