CREATE TABLE images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom_image VARCHAR(255),
    donnees_image LONGBLOB
);


INSERT INTO images (nom_image, donnees_image) 
VALUES ('image1.jpg', LOAD_FILE('/docker-entrypoint-initdb.d/cm1-flc-c13-img02.png'));
