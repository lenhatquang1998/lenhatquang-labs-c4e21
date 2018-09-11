from gmail import GMail, Message

mail = GMail("quangln62@wru.vn", "Lenhatquang1")
msg = Message("xin nghi hoc", to="qhuydtvt@gmail.com", text="tối qua đi bão mệt quá")
mail.send(msg)