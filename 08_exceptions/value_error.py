try:
    num = int(5)
except ZeroDivisionError as e:
    print(f"###Can not divide by zero: {e}")
except ValueError as e:
    print(f"###Invalid number given: {e}")
else:
    print(f"###Conversion successful: {num}")
finally:
    print("###Execution completed.")