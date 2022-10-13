from mftool import Mftool
obj = Mftool()
data = obj.get_scheme_quote('148629')
print(data)
obj.get_scheme_details("119551")
data = obj.get_scheme_historical_nav("119551")
print(data)

