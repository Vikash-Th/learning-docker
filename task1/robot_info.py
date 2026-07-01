import platform, socket, datetime
print('=== Robot Environment Info ===')
print(f'Hostname    : {socket.gethostname()}')
print(f'OS          : {platform.system()} {platform.release()}')
print(f'Python      : {platform.python_version()}')
print(f'Time        : {datetime.datetime.now()}')
print('Running inside Docker!')
