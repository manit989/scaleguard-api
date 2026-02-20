local bucket_key = KEYS[1]
local refill_rate = tonumber(ARGV[1])
local max_tokens = tonumber(ARGV[2])
local current_time = tonumber(ARGV[3])

local data = redis.call('HMGET', bucket_key, 'tokens', 'last_refill_time')
local tokens = tonumber(data[1])
local last_refill_time = tonumber(data[2])

if not tokens then
    tokens = max_tokens
    last_refill_time = current_time
end

local elapsed = math.max(0, current_time - last_refill_time)
local new_tokens = math.floor(elapsed * refill_rate)
tokens = math.min(max_tokens, tokens + new_tokens)

if tokens >= 1 then
    tokens = tokens - 1
    redis.call('HMSET', bucket_key, 'tokens', tokens, 'last_refill_time', current_time)
    return 1 
else
    return 0
end

