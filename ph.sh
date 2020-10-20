echo"..::MEnjalankan local host::.."
echo"[!]INFORMASI[!]"
echo"local host : php"
echo"[!]di versi selanjutnya xampp/lampp akan di tambahkan[!"
echo"masukan nama local hostnya"
echo"ex.localhost:8080, 127.0.0.1:8080"
read nama
echo"masukan dir/file"
read file
php -S $nama $file
