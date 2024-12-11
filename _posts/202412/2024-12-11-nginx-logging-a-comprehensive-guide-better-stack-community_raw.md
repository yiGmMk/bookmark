Title: Nginx Logging: A Comprehensive Guide | Better Stack Community

URL Source: https://betterstack.com/community/guides/logging/how-to-view-and-configure-nginx-access-and-error-logs/

Markdown Content:
[Nginx](https://nginx.org/en/), like most applications, records a wealth of data related to client interactions, system events, and potential errors. However, this data's potential can only be fully realized through proper configuration, management, and analysis.

This article will teach you to effectively customize Nginx logs for enhanced visibility and control over your web servers and proxies. Doing this will help you proactively identify and address issues before they disrupt user experience.

Let's begin!

Prerequisites
-------------

To follow through with this tutorial, you need the following:

*   Basic command-line skills.
*   A Linux system that includes a non-root user with `sudo` privileges.
*   A recent version of [Docker](https://docs.docker.com/engine/install/) installed on your system.

Step 1 — Running Nginx with Docker
----------------------------------

Using the [official Docker image](https://hub.docker.com/_/nginx) is the easiest way to begin working with the Nginx. It simplifies the setup process and ensures consistent reproducibility across different systems.

To get started, create a new `nginx-logging-tutorial` directory, navigate into it, and execute the following `docker run` command: :

```
mkdir nginx-logging-tutorial && cd nginx-logging-tutorial
```

```
docker run --name nginx-server --rm -p 80:80 nginx
```

In this command:

*   `--name nginx-server`: Assigns the `nginx-server` name to the container for easier reference.
*   `--rm`: Automatically removes the container when it's stopped, ideal for testing or temporary setups.
*   `-p 80:80`: Maps port 80 of your host machine to port 80 inside the container, allowing you to access the Nginx server at `http://localhost`.

If the `nginx` image isn't already present on your system, Docker will download it before launching the container.

If you encounter an error like the following:

```
docker: Error response from daemon: driver failed programming external connectivity on endpoint nginx (363e1b33c95786ca6293208b529051a4cf0509208444707b65aef2ddd329ef7e): Bind for 0.0.0.0:80
failed: port is already allocated.
```

It indicates that another application on your system is already using port 80. Ensure that no other services are running on this port before retrying the command.

If Nginx starts successfully, you'll see messages like these in your terminal:

```
. . .
/docker-entrypoint.sh: Configuration complete; ready for start up
2024/08/06 14:47:59 [notice] 1#1: using the "epoll" event method
2024/08/06 14:47:59 [notice] 1#1: nginx/1.27.0
2024/08/06 14:47:59 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14)
2024/08/06 14:47:59 [notice] 1#1: OS: Linux 6.9.12-200.fc40.x86_64
2024/08/06 14:47:59 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1073741816:1073741816
2024/08/06 14:47:59 [notice] 1#1: start worker processes
2024/08/06 14:47:59 [notice] 1#1: start worker process 29
```

Now, open your web browser and navigate to `http://localhost`. You should be greeted by the default Nginx welcome page, confirming that your web server is up and running.

Upon returning to your terminal, you might notice log entries like these:

```
172.17.0.1 - - [06/Aug/2024:14:55:37 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36" "-"
2024/08/06 14:55:37 [error] 29#29: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP /1.1", host: "localhost", referrer: "http://localhost/"
172.17.0.1 - - [06/Aug/2024:14:55:37 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36" "-"
```

These logs reveal that your browser successfully fetched the main webpage but encountered a 404 error when attempting to retrieve the `favicon.ico` file because it's not in the default Nginx directory.

Feel free to stop the Nginx container using `Ctrl-C` before moving on to the next section, where we'll dive deeper into the meaning of these log messages.

Step 2 — Locating the Nginx log files
-------------------------------------

Like most web servers, Nginx meticulously records its activities in two distinct log files:

1.  **Access log**: This file chronicles each incoming request, capturing crucial details such as the client's IP address, the timestamp of the request, the requested resource (URI), the HTTP status code of the response, and the client's user agent (browser and operating system).
    
2.  **Error log**: This file serves as a diagnostic tool, recording errors and issues encountered during request processing and other Nginx operations. It logs information such as the timestamp, error level, error message, and any relevant context to aid troubleshooting.
    

### Locating Nginx logs in different environments

The location of these log files varies depends on your operating system and Nginx installation method.

#### Linux distributions

In most Linux distributions, Nginx log files are typically located in the `/var/log/nginx/` directory. You'll find them named `access.log` and `error.log` respectively.

If you can't find the log files in the default location, you'll need to check your specific Nginx configuration. Start by determining the location of your Nginx configuration file (usually `/etc/nginx/nginx.conf`):

This command should output the location of your configuration file if it's valid:

```
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

Open the configuration file and look for the `error_log` and `access_log` directives to pinpoint their respective locations.

/etc/nginx/nginx.conf

Copied!

```
error_log /var/log/nginx/error.log

http {
  . . .
  access_log  /var/log/nginx/access.log;
  . . .
}
```

By default, Nginx applies the `error_log` directive globally, while the `access_log` is usually placed within the `http` block.

You can use the `tail` command to view the contents of these files in real-time:

```
sudo tail -f /var/log/nginx/access.log
```

```
sudo tail -f /var/log/nginx/error.log
```

#### Docker container

Since Docker containers are ephemeral, it's not practical to store logs directly within the container. The official Nginx Docker image addresses this by creating symbolic links from `/var/log/nginx/access.log` and `/var/log/nginx/error.log` to the container's standard output (`/dev/stdout`) and standard error (`/dev/stderr`) streams respectively. This enables [Docker's logging mechanisms](https://betterstack.com/community/guides/logging/how-to-start-logging-with-docker/) to collect and manage the logs.

You can find the [relevant lines in the Dockerfile](https://github.com/nginxinc/docker-nginx/blob/a6f7d140744f8b15ff4314b8718b3f022efc7f43/mainline/debian/Dockerfile#L105-L107):

mainline/debian/Dockerfile

Copied!

```
. . .
ln -sf /dev/stdout /var/log/nginx/access.log \
&& ln -sf /dev/stderr /var/log/nginx/error.log \
```

Start the `nginx-server` container once again, but detach it from your current terminal session:

```
docker run --name nginx-server -d -p 80:80 nginx
```

```
18394cb59b3e1d334143300e9a86744c2babb6994b5a92782fb92e10098f25b4
```

With the container running, visit `http://localhost` once again to generate some logs, then use the `docker logs` command to view them accordingly:

```
docker logs -f nginx-server
```

You will see the familiar Nginx log output which combines both the access and error logs:

```
. . .
172.17.0.1 - - [06/Aug/2024:16:37:59 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0" "-"
2024/08/06 16:37:59 [error] 31#31: *3 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost", referrer: "http://localhost/"
172.17.0.1 - - [06/Aug/2024:16:37:59 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "http://localhost/" "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0" "-"
```

To view only the access logs, redirect the standard error to `/dev/null`:

```
docker logs -f nginx-server 2>/dev/null
```

```
. . .
172.17.0.1 - - [06/Aug/2024:16:37:59 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0" "-"
172.17.0.1 - - [06/Aug/2024:16:37:59 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "http://localhost/" "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0" "-"
```

Similarly, to view only the error logs, redirect the standard output to `/dev/null`:

```
docker logs -f nginx-server 1>/dev/null
```

```
. . .
2024/08/06 16:37:59 [error] 31#31: *3 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost", referrer: "http://localhost/"
```

Now that you know how to locate and access Nginx log files in various environments, let's explore how you can customize the access log format to suit your needs.

Step 3 — Configuring Nginx access logs
--------------------------------------

By default, Nginx access logs are generated in the `combined` format unless otherwise specified. This format is defined as:

```
'$remote_addr - $remote_user [$time_local] ' '"$request" $status $body_bytes_sent ' '"$http_referer" "$http_user_agent" "$http_x_forwarded_for"';
```

This configuration produces access log entries similar to this:

```
172.17.0.1 - - [06/Aug/2024:16:37:59 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0" "-"
```

Let's break down what each token in the log represents:

*   `172.17.0.1`: The IP address of the client that made the request.
*   `-`: If authentication is used, this is the authenticated username; otherwise, it's a hyphen (-).
*   `[06/Aug/2024:16:37:59 +0000]`: The local time when the request was processed.
*   `"GET / HTTP/1.1"` : The request method, path, and HTTP protocol version.
*   `200`: The HTTP status code returned to the client.
*   `615`: The size of the response body in bytes.
*   `"-"`: The URL of the referring page (if any).
*   `"Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"` - The browser and operating system information provided by the client.
*   `"-"`: If the request passed through a proxy, this variable contains the original client IP address.

While this format captures a wide range of information that is useful for analyzing traffic patterns, troubleshooting errors, and understanding user behavior, you may want to customize it to capture only the data that matters most to you. Let's look at how to do that next.

You can tailor the access log format using the `log_format` directive in either the main Nginx configuration file (`/etc/nginx/nginx.conf`) or within host-specific configurations in `/etc/nginx/sites-enabled`.

If Nginx is running directly on your host machine, you can edit the relevant file accordingly. For Docker instances, execute the command below to extract the Nginx configuration file from the `nginx` image and save it to an `nginx.conf` file on your host machine:

```
docker run --rm --entrypoint=cat nginx /etc/nginx/nginx.conf > nginx.conf
```

Once you're ready to launch the container once again, ensure to mount the modified file from your host machine to `/etc/nginx/nginx.conf` within the container:

```
docker run --name nginx-server -v ./nginx.conf:/etc/nginx/nginx.conf:ro -d nginx
```

### Customizing the access log format

Customizing the format of the entries in the access log can be done using the `log_format` directive:

```
log_format <name> '<formatting_variables>';
```

All you need to do is give the custom format a name and define the structure of the log using the provided [core variables](https://nginx.org/en/docs/http/ngx_http_core_module.html#variables) and [log variables](https://nginx.org/en/docs/http/ngx_http_log_module.html#log_format). Here's an example of what it could look like:

```
. . .
http {
    . . .
    log_format custom '$remote_addr - $remote_user [$time_local]  $status '
                  '"$host" "$request" $body_bytes_sent "$http_referer" '
                  '"$http_user_agent" "$http_x_forwarded_for"';
    . . .
}
```

This example adds the `$host` variable to the combined log format so that it the domain (or subdomain) being requested is also presented in the logs.

To apply this custom format, modify the `access_log` directive:

```
access_log /var/log/nginx/access.log custom;
```

Save your changes, then stop and remove your existing `nginx-server` container with:

```
docker container stop nginx-server
```

```
docker container rm nginx-server
```

Start it again with:

```
docker run --name nginx-server --rm -p 80:80 -v ./nginx.conf:/etc/nginx/nginx.conf:ro nginx
```

When you visit `http://localhost` now, you will observe that the domain is recorded in the corresponding log entry:

```
172.17.0.1 - - [07/Aug/2024:09:32:40 +0000]  404 "localhost" "GET /favicon.ico HTTP/1.1" 555 "http://localhost/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36" "-"
```

### Setting up conditional logging

Nginx's access logs can become quite large, especially under heavy traffic. Conditional logging allows you to selectively filter log entries based on specific criteria to reduce log volume and improve performance.

The syntax looks like this:

```
access_log /path/to/access.log <log_format> if=<condition>;
```

The `<condition>` is a boolean expression that Nginx evaluates for each request. If it evaluates to `true`, the log entry is written; otherwise, it's skipped.

The following example demonstrates how to exclude successful (2xx) and redirection (3xx) status codes from the access log:

```
http {
    map $status $loggable {
        ~^[23]  0;  # Match 2xx and 3xx status codes
        default 1;  # Log everything else
    }

    access_log /var/log/nginx/access.log combined if=$loggable;
}
```

Some practical applications of conditional logging include:

*   Logging only error responses (4xx and 5xx) for troubleshooting.
*   Excluding specific user agents or IP addresses known to be bots.
*   Logging only requests to specific parts of your application.
*   Logging a percentage of requests to [reduce logging costs](https://betterstack.com/community/guides/logging/log-sampling/) while still capturing a representative sample ([see here for some sampling techniques](https://www.f5.com/company/blog/nginx/sampling-requests-with-nginx-conditional-logging)).

### Disabling the access log

If you're already collecting request logs through your web application, you may want to disable the Nginx access log by using a special `off` value, or by redirecting to `/dev/null`

```
access_log off;
access_log /dev/null;
```

Step 4 - Structuring Nginx access logs
--------------------------------------

In the world of cloud-native distributed systems and microservices, [structured logging](https://betterstack.com/community/guides/logging/structured-logging/) has gained significant traction due to its numerous benefits over traditional plain-text logs.

For example, [Caddy](https://betterstack.com/community/guides/web-servers/caddy/), an Nginx alternative, produces access logs that look like this:

```
{
    "level": "info",
    "ts": 1646861401.5241024,
    "logger": "http.log.access",
    "message": "handled request",
    "request": {
        "remote_ip": "127.0.0.1",
        "remote_port": "41342",
        "client_ip": "127.0.0.1",
        "proto": "HTTP/2.0",
        "method": "GET",
        "host": "localhost",
        "uri": "/",
        "headers": {
            "User-Agent": ["curl/7.82.0"],
            "Accept": ["*/*"],
            "Accept-Encoding": ["gzip, deflate, br"],
        },
        "tls": {
            "resumed": false,
            "version": 772,
            "cipher_suite": 4865,
            "proto": "h2",
            "server_name": "example.com"
        }
    },
    "bytes_read": 0,
    "user_id": "",
    "duration": 0.000929675,
    "size": 10900,
    "status": 200,
    "resp_headers": {
        "Server": ["Caddy"],
        "Content-Encoding": ["gzip"],
        "Content-Type": ["text/html; charset=utf-8"],
        "Vary": ["Accept-Encoding"]
    }
}
```

Let's explore how to bring Nginx access logs into this modern era.

While Nginx doesn't natively produce JSON logs, you can achieve this using the `log_format` directive in conjunction with the `escape=json` parameter which ensures that characters that aren't valid in JSON are properly escaped.

Let's see how this works:

```
. . .
http {
    . . .
    log_format custom_json escape=json '{'
        '"level":"info",'
        '"ts": "$time_iso8601",'
        '"message": "handled request $request_method $request_uri",'
        '"request": {'
            '"id": "$http_x_request_id",'
            '"remote_ip": "$remote_addr",'
            '"remote_port": "$remote_port",'
            '"protocol": "$server_protocol",'
            '"method": "$request_method",'
            '"host": "$host",'
            '"uri": "$request_uri",'
            '"headers": {'
                '"user-agent": "$http_user_agent",'
                '"accept": "$http_accept",'
                '"accept-encoding": "$http_accept_encoding",'
                '"traceparent": "$http_traceparent",'
                '"tracestate": "$http_tracestate"'
            '}'
        '},'
        '"bytes_read": $request_length,'
        '"duration_msecs": $request_time,'
        '"size": $bytes_sent,'
        '"status": $status,'
        '"resp_headers": {'
          '"content_length": "$sent_http_content_length",'
          '"content_type": "$sent_http_content_type"'
        '}'
    '}';

    access_log /var/log/nginx/access.log custom_json;
    . . .
}
```

In this configuration:

*   We defined a new log format named `custom_json` and enabled JSON escaping with `escape=json`.
*   Within the JSON structure, we capture a variety of information:
    *   Basic details like log level, timestamp (ts), and a message.
    *   Detailed request information nested under the request object, including headers using `$http_<header_name>`.
    *   Metrics like bytes read, response time, and response size.
    *   Response details like status and specific response headers using `$sent_http_<header_name>`.
*   Finally, the `custom_json` format is applied to the access log.

After saving the configuration and restarting Nginx, make a request with some fictional [distributed tracing headers](https://betterstack.com/community/guides/observability/distributed-tracing/):

```
curl -v -H "traceparent: 00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01" \
     -H "tracestate: rojo=00f067aa0ba902b7" \
     -H "X-Request-Id: f45a82a7-7066-40d4-981d-145952c290f8" \
     http://localhost
```

You'll observe new access log entries in a clean JSON format:

```
{
  "level": "info",
  "ts": "2024-08-07T11:57:31+00:00",
  "message": "handled request GET /",
  "request": {
    "id": "f45a82a7-7066-40d4-981d-145952c290f8",
    "remote_ip": "172.17.0.1",
    "remote_port": "39638",
    "protocol": "HTTP/1.1",
    "method": "GET",
    "host": "localhost",
    "uri": "/",
    "headers": {
      "user-agent": "curl/8.6.0",
      "accept": "*/*",
      "accept-encoding": "",
      "traceparent": "00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01",
      "tracestate": "rojo=00f067aa0ba902b7"
    }
  },
  "bytes_read": 229,
  "duration_msecs": 0.000,
  "size": 853,
  "status": 200,
  "resp_headers": {
    "content_length": "615",
    "content_type": "text/html"
  }
}
```

This structured format makes your logs much easier to parse and analyze, opening the doors to powerful log management and visualization capabilities.

Step 5 — Configuring Nginx error logs
-------------------------------------

The Nginx error log is a crucial tool for diagnosing and resolving issues with your web server. It captures errors, warnings, and other important events that occur during various Nginx operations. Let's explore how to configure and manage this valuable resource.

The `error_log` directive controls Nginx's error logging behavior. It accepts two parameters: the path of the log file, and the minimum [severity level](https://betterstack.com/community/guides/logging/log-levels-explained/) of the log.

```
error_log /var/log/nginx/error.log <severity_level>;
```

Nginx categorizes error log messages into the following levels, ranging from least to most severe:

*   `debug`: Highly detailed messages primarily used for troubleshooting and development.
*   `info`: General informational messages about the server's operation.
*   `notice`: Noteworthy events that aren't necessarily errors.
*   `warn`: Unexpected occurrences that could indicate potential problems.
*   `error`: Actual errors encountered during processing.
*   `crit`: Critical conditions that require attention.
*   `alert`: Errors that demand immediate action.
*   `emerg`: Severe errors that render the system unusable.

If you haven't explicitly configured the error severity level in your Nginx configuration, you will see messages at the `error` level and all levels above it (`crit`, `alert`, and `emerg`). However, the default level for the official Nginx docker image is set to `notice`.

To change the default error log level, provide the desired level as the second parameter to the `error_log` directive:

```
error_log /var/log/nginx/error.log warn;
```

This configuration will log messages at the `warn` level and all higher levels.

### The Nginx error log format

Nginx error logs adhere to a format designed for human readability and easy parsing by tools. The general format is:

```
YYYY/MM/DD HH:MM:SS [<severity_level>] <pid>#<tid>: *<cid> <message>
```

Where:

*   `<pid>`: Process ID
*   `<tid>`: Thread ID
*   `<cid>`: Connection ID

Here's an example of an actual error log entry:

```
2024/08/07 17:41:58 [error] 29#29: *1 open() "/usr/share/nginx/html/make" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /make HTTP/1.1", host: "localhost"
```

### Logging errors to multiple files

Similar to access logs, you can configure Nginx to log errors to multiple files, even with different severity levels:

```
error_log /var/log/nginx/error.log info;
error_log /var/log/nginx/emerg_error.log emerg;
```

In this setup, all events except debug level messages will be logged to `error.log`, while emergency events will be logged to a separate file named `emerg_error.log`.

### Disabling the error log

If you need to completely disable the Nginx error log (though not generally recommended), you can redirect it to `/dev/null`. There doesn't appear to be a special `off` value at the time of writing.

In the next section, we'll look at how you can structure your Nginx error logs in JSON format.

Step 7 — Structuring Nginx error logs
-------------------------------------

While Nginx doesn't offer built-in JSON formatting for its error logs, we can leverage external log processing tools like [Logstash](https://betterstack.com/community/guides/logging/logstash-explained/), [Fluentd](https://betterstack.com/community/guides/logging/fluentd-explained/), or [Vector](https://betterstack.com/community/guides/logging/vector-explained/) to parse, reformat, and enrich these logs for better analysis and integration with modern logging systems.

In this section, I'll demonstrate how to use Vector to transform Nginx error logs into structured JSON format, providing similar benefits to what we achieved with the access logs in the previous step.

If you haven't already, [install Vector on your machine](https://vector.dev/docs/setup/installation/) or pull the [official Docker image](https://hub.docker.com/r/timberio/vector):

```
docker pull timberio/vector:0.40.0-alpine
```

```
0.40.0-alpine: Pulling from timberio/vector
c6a83fedfae6: Already exists
b9fc015ecb16: Pull complete
f7f83e464043: Pull complete
fe91b3a632fb: Pull complete
5312bc41fca9: Pull complete
4f4fb700ef54: Pull complete
Digest: sha256:7a81fdd62e056321055a9e4bdec4073d752ecf68f4c192e676b85001721523c2
Status: Downloaded newer image for timberio/vector:0.40.0-alpine
docker.io/timberio/vector:0.40.0-alpine
```

Next, create a `vector.yaml` file in the current directory with the following contents:

```
sources:
  nginx:
    type: docker_logs
    include_images:
      - nginx

transforms:
  nginx_json:
    type: remap
    inputs:
      - nginx
    source: |
      .context = parse_json(.message) ?? parse_nginx_log(.message, "error") ?? set!(value: {}, path: ["message"], data: .message)
      .message = .context.message
      del(.context.message)
      .

sinks:
  print:
    type: console
    inputs:
      - nginx_json
    encoding:
      codec: json
```

*   `sources`: Defines the log source. In this case, we're collecting logs from Docker containers based on the `nginx` image.
    
*   `transforms`: Defines a transformation named `nginx_json`.
    
    *   `type: remap`: Uses the Vector Remap Language (VRL) for transformation.
    *   `inputs`: Takes input from the `nginx` source.
    *   `source`: Contains the VRL script:
    *   It first attempts to parse the message field as JSON using `parse_json()`.
    *   If that fails, it tries to parse it as an Nginx error log using `parse_nginx_log()`.
    *   If both parsing attempts fail, it creates an empty object and assigns it to `.context.message`.
    *   It then sets the top-level message field to `.context.message` and deletes `.context.message`.
    *   Finally, the `.` at the end returns the modified event.
*   `sinks`: Defines the destination for the transformed logs which is the console in JSON format.
    

**Note for file-based logs**: If you're reading the Nginx logs from files, the `sources` portion should be changed to:

```
sources:
  nginx:
    type: file
    include:
      - /var/log/nginx/error.log
      - /var/log/nginx/access.log

. . .
```

To see this in action, let's bring up both the Nginx and Vector containers with [Docker Compose](https://betterstack.com/community/guides/scaling-docker/docker-compose-getting-started/). Before you proceed, create a `docker-compose.yml` file in your `nginx-logging-tutorial` directory and populate it with the contents below:

docker-compose.yml

Copied!

```
name: nginx-logging-tutorial

services:
  nginx:
    container_name: nginx-server
    image: nginx:alpine
    restart: always
    ports:
      - 80:80
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf

  vector:
    container_name: vector
    image: timberio/vector:0.40.0-alpine
    restart: always
    volumes:
      - ./vector.yaml:/etc/vector/vector.yaml
      - /var/run/docker.sock:/var/run/docker.sock:ro
```

When configuring the vector service in your `docker-compose.yml`, it's necessary to mount the `vector.yaml` file you created into the container to replace the default configuration

You also need to mount the Docker socket (`/var/run/docker.sock`) inside the container. This gives Vector the necessary access to communicate with the Docker daemon, enabling it to identify and monitor the logs of other containers you specify.

However, in a production environment, exposing the Docker socket directly to a container can be a [security risk](https://betterstack.com/community/guides/scaling-docker/docker-security-best-practices/). Consider alternative approaches, such as:

*   Configuring Vector to interact with the Docker daemon over a SSH or HTTPS.
*   Instead of running Vector in a container, install it directly on the host machine to avoid the need for socket mounting.

These precautions help safeguard your Docker environment while still allowing Vector to effectively collect and process your Nginx logs.

To bring up your services, ensure that you've removed the running `nginx-server` container by pressing `CTRL-C` before running the command below:

```
[+] Running 3/3
 ✔ Network nginx-logging-tutorial_default  Created                         0.3s
 ✔ Container nginx-server                  Started                         0.6s
 ✔ Container vector                        Started                         0.6s
```

Navigate back to your browser, access `http://localhost` and refresh the page a couple of times.

You can then view the processed logs with:

If you have [jq](https://github.com/jqlang/jq) installed, you can pipe the output to `jq` while ignoring non-JSON objects with:

```
docker logs -f vector | jq -R 'fromjson? | select(type == "object")'
```

You will see the following output representing an access log:

```
. . .
{
  "container_created_at": "2024-08-08T08:59:06.052457248Z",
  "container_id": "0f17a23cef07616df8cf4f698664e8b9f2c62daaff75bbfc77d750f797eb06c5",
  "container_name": "nginx-server",
"context": {
"bytes_read": 72,
"duration_msecs": 0.0,
"level": "info",
"request": {
"headers": {
"accept": "*/*",
"accept-encoding": "",
"traceparent": "",
"tracestate": "",
"user-agent": "curl/8.6.0"
},
"host": "localhost",
"id": "",
"method": "GET",
"protocol": "HTTP/1.1",
"remote_ip": "172.24.0.1",
"remote_port": "34480",
"uri": "/"
},
"resp_headers": {
"content_length": "615",
"content_type": "text/html"
},
"size": 853,
"status": 200,
"ts": "2024-08-08T11:13:57+00:00"
},
  "host": "3d0ebf54b0eb",
  "image": "nginx:alpine",
  "label": {
    "com.docker.compose.config-hash": "b27d7c9cd09c4f82e419ac408790cbea8ea31a8102d37160b93b318cb4f18cc6",
    "com.docker.compose.container-number": "1",
    "com.docker.compose.depends_on": "",
    "com.docker.compose.image": "sha256:1ae23480369fa4139f6dec668d7a5a941b56ea174e9cf75e09771988fe621c95",
    "com.docker.compose.oneoff": "False",
    "com.docker.compose.project": "nginx-logging-tutorial",
    "com.docker.compose.project.config_files": "/home/ayo/dev/betterstack/demo/nginx-docker/docker-compose.yml",
    "com.docker.compose.project.working_dir": "/home/ayo/dev/betterstack/demo/nginx-docker",
    "com.docker.compose.service": "nginx",
    "com.docker.compose.version": "2.29.1",
    "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
  },
  "message": "handled request GET /",
  "source_type": "docker_logs",
  "stream": "stdout",
  "timestamp": "2024-08-08T11:13:57.834369885Z"
}
```

The `context` property contains the original JSON object from Nginx as parsed by the `parse_json()` function we used earlier. The other properties were added by Vector when collecting the logs from the Docker container.

To what see a parsed error log, you can make a request for a non-existent file with:

```
curl http://localhost/favicon.ico
```

You will subsequently observe the following entry in the Docker logs:

```
{
    "container_created_at": "2024-08-08T08:59:06.052457248Z",
    "container_id": "0f17a23cef07616df8cf4f698664e8b9f2c62daaff75bbfc77d750f797eb06c5",
    "container_name": "nginx-server",
    "context": {
        "cid": 1,
        "client": "172.24.0.1",
        "host": "localhost",
        "pid": 23,
        "request": "GET /favicon.ico HTTP/1.1",
        "server": "localhost",
        "severity": "error",
        "tid": 23,
        "timestamp": "2024-08-08T16:37:59Z"
    },
    "host": "3d0ebf54b0eb",
    "image": "nginx:alpine",
    "label": {
        "com.docker.compose.config-hash": "b27d7c9cd09c4f82e419ac408790cbea8ea31a8102d37160b93b318cb4f18cc6",
        "com.docker.compose.container-number": "1",
        "com.docker.compose.depends_on": "",
        "com.docker.compose.image": "sha256:1ae23480369fa4139f6dec668d7a5a941b56ea174e9cf75e09771988fe621c95",
        "com.docker.compose.oneoff": "False",
        "com.docker.compose.project": "nginx-logging-tutorial",
        "com.docker.compose.project.config_files": "/home/ayo/dev/betterstack/demo/nginx-docker/docker-compose.yml",
        "com.docker.compose.project.working_dir": "/home/ayo/dev/betterstack/demo/nginx-docker",
        "com.docker.compose.service": "nginx",
        "com.docker.compose.version": "2.29.1",
        "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
    },
    "message": "open() \"/usr/share/nginx/html/favicon.ico\" failed (2: No such file or directory)",
    "source_type": "docker_logs",
    "stream": "stderr",
    "timestamp": "2024-08-08T16:37:59.012