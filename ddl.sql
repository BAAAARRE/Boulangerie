-- auto-generated definition
create table Appareils
(
    ID_Appareils int auto_increment
        primary key,
    libelle      varchar(45) not null,
    constraint ID_Appareils_UNIQUE
        unique (ID_Appareils),
    constraint libelle_UNIQUE
        unique (libelle)
);

-- auto-generated definition
create table Appareils2Etape
(
    ID_Appareils int not null,
    ID_Etape     int not null,
    primary key (ID_Appareils, ID_Etape),
    constraint FK_ID_AppareilsA2E
        foreign key (ID_Appareils) references Appareils (ID_Appareils),
    constraint FK_ID_EtapeA2E
        foreign key (ID_Etape) references Etape (ID_Etape)
);

create index FK_ID_EtapeA2E_idx
    on Appareils2Etape (ID_Etape);

-- auto-generated definition
create table Etape
(
    ID_Etape    int auto_increment
        primary key,
    libelle     varchar(45)  not null,
    description varchar(500) not null,
    temps       int          null,
    ID_Recette  int          not null,
    constraint ID_Etape_UNIQUE
        unique (ID_Etape),
    constraint FK_ID_RecetteEtape
        foreign key (ID_Recette) references Recette (ID_Recette)
);

create index ID_Recette_idx
    on Etape (ID_Recette);

-- auto-generated definition
create table Ingredients
(
    ID_Ingredients int auto_increment
        primary key,
    libelle        varchar(45) not null,
    mesure         varchar(45) not null,
    quantite       int         not null,
    ID_Recette     int         not null,
    constraint ID_Ingredients_UNIQUE
        unique (ID_Ingredients),
    constraint FK_ID_RecetteIngredient
        foreign key (ID_Recette) references Recette (ID_Recette)
);

create index ID_Recette_idx
    on Ingredients (ID_Recette);

-- auto-generated definition
create table Recette
(
    ID_Recette  int auto_increment
        primary key,
    Libelle     varchar(45)  not null,
    Description varchar(45)  not null,
    url_image   varchar(500) null,
    constraint Description_UNIQUE
        unique (Description),
    constraint ID_Recette_UNIQUE
        unique (ID_Recette),
    constraint Libelle_UNIQUE
        unique (Libelle),
    constraint url_image_UNIQUE
        unique (url_image)
);

-- auto-generated definition
create table Ustensile
(
    ID_Ustensile int auto_increment
        primary key,
    type         varchar(45) not null,
    constraint ID_Ustensile_UNIQUE
        unique (ID_Ustensile),
    constraint type_UNIQUE
        unique (type)
);

-- auto-generated definition
create table Ustensile2Etape
(
    ID_Etape     int not null,
    ID_Ustensile int not null,
    primary key (ID_Etape, ID_Ustensile),
    constraint FK_ID_EtapeU2E
        foreign key (ID_Etape) references Etape (ID_Etape),
    constraint FK_ID_UstensileU2E
        foreign key (ID_Ustensile) references Ustensile (ID_Ustensile)
);

create index FK_ID_UstensileU2E_idx
    on Ustensile2Etape (ID_Ustensile);

