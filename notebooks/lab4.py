import threading, time

def function1(name):
	for i in range(100000):
		time.sleep(0.0001)
	print(f'Function: "{name}" has finished excecuting. ')

def function2(times):
	currentTime = time.time()
	elapsedTime = -1
	for i in range(times):
		function1(i)
	elapsedTime = time.time() - currentTime
	print(f'First function excecuted sequentially {times} times in {elapsedTime} seconds. ')

def function3(times):
	currentTime = time.time()
	elapsedTime = -1
	for i in range(times):
		t = threading.Thread(target = function1, name = 'thread1', args = [i])
		t.start()
	elapsedTime = time.time() - currentTime
	print(f'First function excecuted concurrently {times} times in {elapsedTime} seconds. ')

function2(10)
function3(10)