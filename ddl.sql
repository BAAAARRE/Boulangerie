drop table if exists Recette;

create table Recette
(
    id_recette  int auto_increment,
    libelle     text     not null,
    description text     null,
    url_image   text     null,
    constraint Recette_pk
        primary key (id_recette)
);

create unique index Recette_id_recette_uindex
    on Recette (id_recette);

create unique index Recette_libelle_uindex
    on Recette (libelle);


drop table if exists etape;

create table etape
(
    id_etape    int auto_increment,
    libelle     text not null,
    description text not null,
    temps       int  not null,
    quantite    int  not null,
    constraint etape_pk
        primary key (id_etape)
);

create unique index etape_id_etape_uindex
    on etape (id_etape);

