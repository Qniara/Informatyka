 <?php
 $conn = new mysqli("localhost", "root", "");
 $data=[];
foreach($csvfile as $line){
    $data[] = str_getcsv($line);
}
foreach($data as $dt){
    $wiersz = str_getcsv($dt[0],";");
    $insert = "INSERT INTO Kierowcy(idOsoby, Imie, Nazwisko, NrRejestracyjny) VALUES ('.$wiersz[0] .', "' .$wiersz[1] . '")";
}
