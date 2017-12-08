"""Docstrings are dumb"""

import praw



if __name__ == '__main__':

  def dumbstuff(comment: str) -> str:
    message = ''
    lol = "\n\n Hi I am a bot. I don't work that well yet, ignore me please :)"

    if 'me too thanks' in comment.lower():
      message = 'meme too dank' + lol
    if 'metoothanks' in comment.lower():
      message = 'memetoodank' + lol

    return message


  for retarded_reply in multicomments:                  # Change this line for multi
    send = dumbstuff(str(retarded_reply.body))
    if send != '':
      retarded_reply.reply(send)
