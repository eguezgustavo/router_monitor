local internet_connection = {}
local INTERNET_SERVER = "www.google.com"

local function ping()
    local handler = io.popen("ping -c 1 " .. INTERNET_SERVER)
    local response = handler:read("*a")
    
    local time
    local loss
    
    time = nil
    loss = nil

    for token in string.gmatch(response, "[^%s]+") do
        if token:find("%%") then
            loss = token:gsub("%%", "")
            loss = tonumber(loss)
        end
        if token:find("time=") then
            time = token:gsub("time=", "")
            time = tonumber(time)
        end
    end

    return loss, time
end

internet_connection.ping = ping

return internet_connection