from pyrogram import Client, filters
app = Client("sessigwgon_name" ,
                    api_id = '6033447',
                    api_hash = '7f459302a4186c65aa5a4ccdd975ede2')
                    
@app.on_message(filters.command(['py3'],None), filters.me)
def py_me(client, message):
    msg = str(message.text[3:])
    exec(msg)
app.run()
