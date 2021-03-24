# Stupid Dc

Stupid Dc

Stupid meaning "stupidity, a lack of intelligence".

Dc(大创) meaning "innovation project of undergraduate".

**a lack-of-intelligence innovation project of undergraduate**

this project contain three parts
1. pc server
2. pi server
3. flask server

## pc server
pc(or computer with nice cpu/gpu) as server, raspberry pi(with a camera) as client.

Using UDP protocol, client continually read camera, sending frames to pc for classification.

## pi server

raspberry pi as server, pc as client.

Using TCP protocol, server waiting for client's msg to stop a servo inside the closet.

## flask server

pc as server, user devices(such as phone/pc, anything with a web browser).

base on flask framework, it's able to add clothes, delete clothes, select clothes and etc.