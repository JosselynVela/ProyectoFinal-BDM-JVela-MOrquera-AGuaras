# ProyectoFinal-BDM-JVela-MOrquera-AGuaras

Para este proyecto se usaron
<br>
*Dos base de datos relacionales
<br>
*Una base de datos relacional
<br>
*WebScraping
<br>

Los casos de Estudio para este proyecto
<br>
*Trafico en Ecuador
<br>
*Politica
<br>
*Eventos Publicos
<br>
*Trafico en Ecuador
<br>
*Politica
<br>
*Post Facebook
<br>
*Restaurantes
<br>
*Top de las 100 mejores canciones del mundo
<br>
*10 Twitteros mas famosos en Ecuador
<br>
*Politica
<br>
*Noticias del mundo
<h1>Las Herramientas que se usaron fueron:<h/2>
 <ul>
   <li>CouchDb
   <li>MongoDB
    <li>MySQL
   <li>WebScraping
     <li>Kibana
    <
 </ul>
  
  <h1>Extraccion de Datos</h1>
  <h2>Extraccion de Tweets</h2>
  <p>Con nuestro scrypt lo que hicimos fue filtrat por palabras y por geolocalizacion, para que nos funciones deberemos crear una api en twitter, que nos dara tres tipos de credenciales</p>
  <p>Nuestro Script esta disponiible en la carpeta Scripts</p>
  <h2>Extraccion de Datos de Facebook</h2>
  <p>De la misma manera el script esta disponible en nuestra carpeta. Para que nuestro script se ejecute correctamente lo que usamos 
  fue el id de una pagina que ya teniamos creada en facebook</p>
  <h2>Extraccion de Paginas WEB</H3>
  <p>Para esto usamos dos herramientas de Webscraping que son:</p>
  <br>
  <a>
    <li>import.io
    <li>PowerBI
   </a>
   <p>Puede acceder a esta herramienta Online y es gratuita https://www.import.io/<br>
Todas estas url que analizaremos en import y power podremos exportar csv,xsl,xsls,etx</p>

<h2>Exportar Datos</h2>
<p>Para exportar nuestros datos usaremos Logstash que sera quien nos ayude a aneviar nuestra informacion a elasticsearch que fue elegido como contenedor de nuestros datos.Tendremos que configurar nuestro archivo confort. Para nuestros primeros casos de uso lo hemos usado los ejemplos esta en nuestra carpeta Ejecutables</p>
<p>Nosotros pasamos nuestros datos  CouchDB, MOngodb y Mysql
  <p>Tambien tenemos otra herramienta llamda excelastic que es una herramienta de elasticsearc y nos ayuda a pasar nuestro archivo a Kibana para crear nuestra visualisaciones.
 


  
  
  
