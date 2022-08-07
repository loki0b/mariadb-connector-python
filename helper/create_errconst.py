#
# script for creating error constants
#

import requests

ignore_definitions = ["ERR_ERROR_FIRST", "ER_ERROR_LAST", "CR_MIN_ERROR",
                      "CR_MAX_ERROR", "CLIENT_ERRMAP",
                      "CER_MIN_ERROR", "CER_MAX_ERROR",
                      "CR_MYSQL_LAST_ERROR", "CR_MARIADB_LAST_ERROR"]

files = ["https://raw.githubusercontent.com/mariadb-corporation/"
         "mariadb-connector-c/3.3/include/mysqld_error.h",
         "https://raw.githubusercontent.com/mariadb-corporation/"
         "mariadb-connector-c/3.3/include/errmsg.h"]

error_definitions = []

for i in range(0, len(files)):
    errors = requests.get(files[i], allow_redirects=True)
    error_definitions += errors.content.decode("utf8").split("\n")

print("# Autogenerated file. Please do not edit!\n\n")

for i in range(0, len(error_definitions)):
    x = error_definitions[i].split()
    if (len(x) >= 3 and x[0] == "#define" and x[1] not in ignore_definitions
       and x[1][:9] != "ER_UNUSED"):
        try:
            if int(x[2]) > 0:
                print("%s = %s" % (x[1], x[2]))
        except Exception:
            pass
