import  internet, module

internet.connect_wifi("IoT_lab","password123")
internet.send_data("Temperature = 25c")
module.greet()