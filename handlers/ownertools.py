from helpers.dbtools import main_broadcast_handler

@Client.on_message(
    filters.private
    & filters.command("broadcast")
    & filters.user(OWNER_ID)
    & filters.reply
)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)


@Client.on_message(filters.private & filters.command("block"))
@sudo_users_only
async def ban(c: Client, m: Message):
    if len(m.command) == 1:
        await m.reply_text(
            "» this command for ban user from using your bot, read /help for more info !",
            quote=True,
        )
        return
    try:
        user_id = int(m.command[1])
        ban_duration = m.command[2]
        ban_reason = " ".join(m.command[3:])
        ban_log_text = f"🔁 banning user... \n\nuser id: `{user_id}` \nduration: `{ban_duration}` \nreason: `{ban_reason}`"
        try:
            await c.send_message(
                user_id,
                f"sorry, you're banned!** \n\nreason: `{ban_reason}` \nduration: `{ban_duration}` day(s). \n\n**💬 message from owner: ask in @{GROUP_SUPPORT} if you think this was an mistake.",
            )
            ban_log_text += "\n\n✅ this notification was sent to that user"
        except:
            traceback.print_exc()
            ban_log_text += f"\n\n❌ **failed sent this notification to that user** \n\n`{traceback.format_exc()}`"
        await db.ban_user(user_id, ban_duration, ban_reason)
        print(ban_log_text)
        await m.reply_text(ban_log_text, quote=True)
    except:
        traceback.print_exc()
        await m.reply_text(
            f"❌ an error occoured, traceback is given below:\n\n`{traceback.format_exc()}`",
            quote=True,
        )