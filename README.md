Proyecto SmartHome:

Este proyecto consiste en una aplicación de consola escrita en Python para la gestión de dispositivos inteligentes en un hogar. Forma parte del desarrollo del Proyecto Integrador del Módulo Programador. El enofque está en la modularidad, la automatizacion y los principios éticos de desarrollo de Software.

Nuestro equipo de trabajo se encuentra conformado de la siguiente manera:
Gisela Reyna - Carolina Vanucci en Base de Datos
Francisco Serafini - Valdivia Jesica en Programación
Hartl Ana - Faustino Sbezzi en Ética y Deontología

Esta ha sido la organización  definida para obtener un flujo de trabajo que permita avanzar de manera satisfactoria con las entregas planteadas, sin embargo todos los miembros del equipo estamos interiorizados en el trabajo del resto para dar un enfoque global a las soluciones que buscamos traer con este proyecto de desarrollo.

El objetivo del Proyecto es desarrollar un sistema que permita lo siguiente:

- Registrar y gestionar dispositivos inteligentes (luces, cámaras, electrodomésticos, etc).
- Consultar el estado actual de los dispositivos.
- Activar automatizaciones programadas por el usuario.

  Automatización implementada: "Modo despertar"

  El "Modo despertar" es una automatización personalizada que simula una rutina matutina. Cuando el usuario lo activa, el sistema enciende automaticamente dos dispositivos:
   - El **televisor**, para brindar información visual o entretenimiento (a elección del usuario)
   - El **sistema de música** del hogar.

Esta automatización busca generar comodidad al despertar, para que el usuario comience el día de la mejor manera.

La lógica de funcionamiento de dicha automatización es la siguiente:

1. El usuario accede al menú principal y selecciona la opción "Activar Modo Despertador".
2. El sistema verifica si los dispositivos necesarios ("TV" y "Sistema de Música") están registrados.
3. Si existen, se configura en que horario el estado de ambos dispositivos se cambia a "encendido".
4. Se notifica al usuario que el modo ha sido activado.

La Implementación técnica se encuentra en el módulo "automatizaciones.py"
