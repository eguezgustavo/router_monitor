local internet_connection = require('internet_connection')
local http = require("socket.http")

local loss, time = internet_connection.ping()

print("{\"loss\": " ..loss .. ", \"time\": " .. time .. "}")
