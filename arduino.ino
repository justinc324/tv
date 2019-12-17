#include <WiFi.h>
#include <WebServer.h>
#include <WiFiUdp.h>
// #include <OSCMessage.h>


/* Put your SSID & Password */
const char* ssid = "ESP32_jcong";  // Enter SSID here
const char* password = "christmas";  //Enter Password here


/* Put IP Address details */
IPAddress local_ip(192,168,1,1);
IPAddress gateway(192,168,1,1);
IPAddress subnet(255,255,255,0);

WebServer server(80);

WiFiUDP udp;

// light stuff
#define flexSensor 34
#define Vibration 22
#define Switch 25
const char* message = "DEFAULT";

void setup() {
  pinMode(Vibration, INPUT);
  pinMode(Vibration, INPUT_PULLUP);
  Serial.begin(9600);
  WiFi.softAP(ssid, password);
  WiFi.softAPConfig(local_ip, gateway, subnet);
  
    server.begin();

}

int v;
int prev_state = digitalRead(Switch);
int switch_state;

void loop(){
  
  v = digitalRead(Vibration);

  udp.beginPacket("192.168.1.2",57222);
  udp.printf("%i", v);
  udp.endPacket();
  Serial.print(v);

  switch_state = digitalRead(Switch);
  if (switch_state == LOW && switch_state != prev_state) {
    
    Serial.println(-1);
    udp.beginPacket("192.168.1.2",57222);
    udp.printf("%i", -1);
    udp.endPacket();
    prev_state = LOW;
  }

   if (switch_state == HIGH && switch_state != prev_state) {
    
     Serial.println(-2);
    udp.beginPacket("192.168.1.2",57222);
    udp.printf("%i", -2);
    udp.endPacket();
    prev_state = HIGH;
  }
 
  //Wait for .75 second
  delay(500);
  
}
