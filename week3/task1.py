for i in range(100):
    print(f"0{i}" if i<10 else f"{i}",end=", " if i<99 else "\n")