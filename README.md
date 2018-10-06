# snapchat
> Unofficial SnapChat API

### SnapChat(username)

```python
>>> from snapchat import SnapChat
>>> myFriend = SnapChat("mannbilly")
```

### snapcode(bitmoji=False, size=None)
```python
>>> from snapchat import SnapChat
>>> 
>>> myFriend = SnapChat("mannbilly")
>>> myFriend.snapcode(bitmoji=True)
'https://app.snapchat.com/web/deeplink/snapcode?username=mannbilly&type=SVG'
>>> myFriend.snapcode(size=500)
('https://app.snapchat.com/web/deeplink/snapcode?username=mannbilly&type=PNG&size=500', '500x500')
```
Unfortuneatly at the moment, you cant resize a snapcode with a Bitmoji.
