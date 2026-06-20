import json
import urllib.request
import os
import sys

API_KEY = os.environ.get("INTEGRATIONS_API_KEY")
if not API_KEY:
    print("No API KEY")
    sys.exit(1)

en_dict = {
    "select_language": "🌍 *Select Language*",
    "lang_selected": "✅ English language selected!",
    "start_text": "⛀⛂ *Welcome to Saski Bot!*\n\n🎯 8×8 classic checkers — play against the bot, online, or with a friend!\n🏆 ELO rating system • ⚡ Real-time updates • ⏱ 60s/move\n\n📖 Type /help for full rules.\n👇 Select a mode from the menu below:",
    "info": "⛀⛂ *Welcome to Saski Bot!*\n\n🎯 8×8 classic checkers — play against the bot, online, or with a friend!\n🏆 ELO rating system • ⚡ Real-time updates • ⏱ 60s/move\n\n📖 Type /help for full rules.\n👇 Select a mode from the menu below:",
    "btn_profile": "👤 My Profile",
    "btn_bot": "🤖 Play vs Bot",
    "btn_online": "🌐 Play Online",
    "btn_friend": "🤝 Play with Friend",
    "btn_rating": "🏆 Rating",
    "btn_other_bots": "📢 Our Channel",
    "btn_add_group": "➕ Add to Group",
    "btn_change_lang": "🌍 Change Language",
    "btn_back": "⬅️ Back",
    "btn_surrender": "🏳️ Surrender",
    "btn_draw": "🤝 Draw",
    "profile_text": "👤 <b>Profile: {name}</b>\n\n🏆 <b>Rating:</b> {elo} ELO\n🎮 <b>Games played:</b> {total_games}\n✅ <b>Wins:</b> {wins}\n❌ <b>Losses:</b> {losses}\n🤝 <b>Draws:</b> {draws}",
    "bot_label": "🤖 Bot",
    "waiting_player": "⏳ Waiting...",
    "mode_bot": "🤖 Bot Mode",
    "mode_pvp": "🌐 Online Mode",
    "mode_friend": "🤝 Friend Mode",
    "board_header": "🎮 <b>{mode}</b>\n⚪️ {white}  🆚  ⚫️ {black}\n",
    "turn_white": "⏳ <b>White's turn:</b> {name} ({sec}s)",
    "turn_black": "⏳ <b>Black's turn:</b> {name} ({sec}s)",
    "not_registered": "Please type /saski to register first.",
    "not_participant": "You are not participating in this game.",
    "err_not_your_turn": "It's not your turn!",
    "err_invalid_move": "Invalid move!",
    "err_chain_jump": "You must continue jumping with the same piece!",
    "err_king_promoted_chain": "Promoted to King! Your turn ends.",
    "piece_selected": "Piece selected 🟢",
    "game_over_surrender": "\n\n🏳️ <b>Game Over — {winner} Wins!</b>\n{loser} surrendered.\n\n📈 <b>ELO Changes:</b>\n{elo_changes}\n\n👇 Use /saski for a new game.",
    "game_over_win": "\n\n🎉 <b>Game Over — {winner} Wins!</b>\n\n📈 <b>ELO Changes:</b>\n{elo_changes}\n\n👇 Use /saski for a new game.",
    "game_over_draw": "\n\n🤝 <b>Game Over — Draw!</b>\n\n📈 <b>ELO Changes:</b>\n{elo_changes}\n\n👇 Use /saski for a new game.",
    "game_over_timeout": "\n\n⏱ <b>Game Over — {winner} Wins!</b>\n{loser} ran out of time.\n\n📈 <b>ELO Changes:</b>\n{elo_changes}\n\n👇 Use /saski for a new game.",
    "draw_proposed": "\n\n❓ {name} proposed a draw.",
    "draw_rejected": "\n\n❌ {name} rejected the draw.",
    "elo_change_row": "👤 <b>{name}</b>: {old} → {new} ({diff})",
    "bot_surrendered": "\n\n🏳️ <b>Game Over — You Win!</b>\nBot surrendered.\nℹ️ Bot games do not affect statistics.\n\n👇 Use /saski for a new game.",
    "you_surrendered": "\n\n🏳️ <b>Game Over — You Lose!</b>\nYou surrendered against the bot.\nℹ️ Bot games do not affect statistics.\n\n👇 Use /saski for a new game.",
    "bot_won": "\n\n🎉 <b>Game Over — Bot Wins!</b>\nℹ️ Bot games do not affect statistics.\n\n👇 Use /saski for a new game.",
    "you_won": "\n\n🎉 <b>Game Over — You Win!</b>\nℹ️ Bot games do not affect statistics.\n\n👇 Use /saski for a new game.",
    "bot_draw": "\n\n🤝 <b>Game Over — Draw!</b>\nℹ️ Bot games do not affect statistics.\n\n👇 Use /saski for a new game.",
    "btn_agree": "✅ Agree",
    "btn_reject": "❌ Reject",
    "already_proposed": "You have already proposed a draw. Waiting for response.",
    "online_search_msg": "🌐 <b>Online Matching</b>\n\nSearching for an opponent... ⏳\n<i>(Please wait, do not press multiple times)</i>",
    "online_cancelled": "❌ Search cancelled.",
    "btn_cancel": "❌ Cancel",
    "friend_invite_msg": "🤝 <b>Play with Friend</b>\n\nForward this message to a friend or group, or choose from the list below.",
    "btn_select_chat": "Share Game",
    "friend_pick_color_text": "🤝 <b>Play with Friend</b>\n\nChoose your color:\n⚪️ White: {white}\n⚫️ Black: {black}\n\n<i>Click the same color again to start if both are selected.</i>",
    "btn_white": "⚪️ White",
    "btn_black": "⚫️ Black",
    "btn_start_game": "▶️ Start",
    "color_already_taken": "This color is already taken by the other player!",
    "both_must_choose": "Both players must select a color before starting!",
    "group_waiting_color": "⏳ Waiting...",
    "group_color_select_msg": "🤝 <b>Friend Match</b>\n\nChoose your colors:\n⚪️ White: {white}\n⚫️ Black: {black}",
    "group_lang_changed": "Language changed to English.",
    "btn_lang": "{lang}",
    "rating_menu": "🏆 <b>Rating Menu</b>\n\nChoose a category:",
    "btn_top_elo": "📈 Top ELO",
    "btn_top_wins": "🏅 Top Wins",
    "top_elo_title": "📈 <b>Top 20 ELO Rating</b>\n\n",
    "top_wins_title": "🏅 <b>Top 20 Wins</b>\n\n",
    "rating_row_elo": "<b>{idx}.</b> {name} — 🏆 {val} ELO\n",
    "rating_row_wins": "<b>{idx}.</b> {name} — 🏆 {val} wins\n",
    "help_text": "⛀⛂ <b>Saski Bot Rules & Info</b>\n\n<b>1. Movement:</b>\nPieces move diagonally forward 1 step. Kings can move diagonally backwards.\n\n<b>2. Capturing:</b>\nJumping over an opponent's piece is <b>mandatory</b>. If you can jump, you must.\n\n<b>3. Chain Jumping:</b>\nIf you can jump again after capturing, you must continue the chain.\n\n<b>4. Timer:</b>\nEach player has 60 seconds per move. If you run out of time, you lose.\n\n<b>5. Modes:</b>\n🤖 Bot: Practice against AI.\n🌐 Online: Match with a random player.\n🤝 Friend: Play with a specific person in private or group chats.\n\n<b>6. ELO Rating:</b>\nYou start with 1000 ELO. Winning increases your rating, losing decreases it."
}

languages = {
    "tr": "Turkish (Türkiye Türkçesi)",
    "kk": "Kazakh (Қазақ тілі)",
    "ky": "Kyrgyz (Кыргыз тили)",
    "hi": "Hindi (हिन्दी)",
    "uz": "Uzbek (O'zbek tili)",
    "ar": "Arabic (العربية)",
    "id": "Indonesian (Bahasa Indonesia)",
    "lt": "Lithuanian (Lietuvių kalba)"
}

prompt = f"""
I have a JSON dictionary of UI strings for a Checkers (Dama) Telegram bot in English.
Translate this dictionary into the following 8 languages, returning ONLY a valid JSON object containing the translations.
For each language code, provide the full translated dictionary.
The result must have this structure:
{{
  "tr": {{ ... }},
  "kk": {{ ... }},
  "ky": {{ ... }},
  "hi": {{ ... }},
  "uz": {{ ... }},
  "ar": {{ ... }},
  "id": {{ ... }},
  "lt": {{ ... }}
}}

Rules:
1. Translate contextually for a Telegram Bot interface playing Checkers.
2. The name of the game "Saski" should be translated contextually (e.g. "Dama" in Turkish, "Шашки" in Kyrgyz/Kazakh, "Checkers" in Hindi, etc. Or just "Saski (Dama)" etc.).
3. KEEP all placeholders exactly as they are: {{name}}, {{idx}}, {{val}}, {{sec}}, {{elo}}, {{total_games}}, {{wins}}, {{losses}}, {{draws}}, {{mode}}, {{white}}, {{black}}, {{winner}}, {{loser}}, {{elo_changes}}, {{diff}}, {{old}}, {{new}}, {{lang}}.
4. KEEP all emojis exactly as they are.
5. KEEP all HTML tags (<b>, <i>, etc.) exactly as they are.
6. The command /saski and /help should NOT be translated.
7. Return ONLY the raw JSON string. Do not use Markdown code blocks like ```json ... ```. Just the JSON object starting with {{ and ending with }}.

English Dictionary:
{json.dumps(en_dict, indent=2)}
"""

req_body = {
    "contents": [
        {
            "role": "user",
            "parts": [{"text": prompt}]
        }
    ]
}

req = urllib.request.Request(
    "https://app-cej2tb5o4l4x-api-VaOwP8E7dJqa.gateway.appmedo.com/v1beta/models/gemini-2.5-flash:streamGenerateContent?alt=sse",
    data=json.dumps(req_body).encode('utf-8'),
    headers={
        "Content-Type": "application/json",
        "X-Gateway-Authorization": f"Bearer {API_KEY}"
    },
    method="POST"
)

response_text = ""
try:
    with urllib.request.urlopen(req) as response:
        for line in response:
            line = line.decode('utf-8').strip()
            if line.startswith("data: "):
                data_str = line[6:]
                if data_str == "[DONE]":
                    break
                try:
                    data = json.loads(data_str)
                    if "candidates" in data and len(data["candidates"]) > 0:
                        part = data["candidates"][0]["content"]["parts"][0]
                        if "text" in part:
                            response_text += part["text"]
                except Exception as e:
                    pass
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

response_text = response_text.replace("```json", "").replace("```", "").strip()

try:
    translated_dict = json.loads(response_text)
    with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/translated_locales.json", "w", encoding="utf-8") as f:
        json.dump(translated_dict, f, ensure_ascii=False, indent=4)
    print("Translation completed successfully.")
except Exception as e:
    print(f"Failed to parse JSON: {e}")
    with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/failed_translation.txt", "w", encoding="utf-8") as f:
        f.write(response_text)
