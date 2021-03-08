CREATE TABLE IF NOT EXISTS guild_settings(
    guild_id BIGINT PRIMARY KEY,
    prefix VARCHAR(30)
);


CREATE TABLE IF NOT EXISTS user_settings(
    user_id BIGINT PRIMARY KEY,
    timezone_offset INTEGER
);


CREATE TABLE IF NOT EXISTS role_list(
    guild_id BIGINT,
    role_id BIGINT,
    key VARCHAR(50),
    value VARCHAR(50),
    PRIMARY KEY (guild_id, role_id, key)
);


CREATE TABLE IF NOT EXISTS channel_list(
    guild_id BIGINT,
    channel_id BIGINT,
    key VARCHAR(50),
    value VARCHAR(50),
    PRIMARY KEY (guild_id, channel_id, key)
);

CREATE TABLE IF NOT EXISTS modlogs(
    guild_id BIGINT PRIMARY KEY,
    modlog_channel BIGINT
);

CREATE TABLE IF NOT EXISTS roles(
    message_id BIGINT,
    emoji VARCHAR(100),
    role_id BIGINT,
    PRIMARY KEY (message_id, emoji)
);
