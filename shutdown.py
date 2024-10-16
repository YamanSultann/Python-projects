shut = input("Do you want to shut down? (yes/no): ")

if shut == "yes" or shut == "Yes":
    downloads = input("Are there any downloads running? (yes/no): ")
    if downloads == "no" or downloads == "No":
        bgprogs = input("Are there any programs running in the background? (yes/no): ")
        if bgprogs == "no" or bgprogs == "No":
            apps = input("Are there any apps running? (yes/no): ")
            if apps == "no" or apps == "No":
                progs = input("Are there any programns running? (yes/no): ")
                if progs == "no" or progs == "No":
                    shutdown = input("Type 'Okay' to shutdown")
                else:
                    print("Sorry can't shutdown")
            else:
                print("Sorry can't shutdown")
        else:
            print("Sorry can't shutdown")
    else:
        print("Sorry can't shutdown")
else:
    print("Sorry can't shutdown")