extension = input("file name: ").strip()

len = extension.count(".")

extension = extension.split(".")[len]

match extension:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf" | "PDF":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case "bin":
        print("application/octet-stream")
    case _:
        print("application/octet-stream")