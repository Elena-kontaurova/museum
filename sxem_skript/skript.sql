-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema franprof
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema franprof
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `franprof` DEFAULT CHARACTER SET utf8mb3 ;
-- -----------------------------------------------------
-- Schema musuem
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema musuem
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `musuem` DEFAULT CHARACTER SET utf8mb3 ;
USE `franprof` ;

-- -----------------------------------------------------
-- Table `franprof`.`autorizregus`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`autorizregus` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `role` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 12
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`denech_sredst`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`denech_sredst` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `one_den` VARCHAR(255) NOT NULL,
  `two_den` VARCHAR(255) NOT NULL,
  `three_den` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`dop`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`dop` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name_l` VARCHAR(255) NOT NULL,
  `last` VARCHAR(255) NOT NULL,
  `name_r` VARCHAR(255) NOT NULL,
  `rel` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`forma_str1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`forma_str1` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `data_zac` VARCHAR(255) NOT NULL,
  `data_doc` VARCHAR(255) NOT NULL,
  `kol_vo` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`forma_str2`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`forma_str2` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `data_zac` VARCHAR(255) NOT NULL,
  `data_doc` VARCHAR(255) NOT NULL,
  `kol_vo` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`forma_str3`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`forma_str3` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `data_zac` VARCHAR(255) NOT NULL,
  `data_doc` VARCHAR(255) NOT NULL,
  `kol_vo` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`inform_status`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`inform_status` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `podk` VARCHAR(255) NOT NULL,
  `nastr` VARCHAR(255) NOT NULL,
  `oblak` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 93
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`kompany`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`kompany` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `veshe` VARCHAR(255) NOT NULL,
  `adres` VARCHAR(255) NOT NULL,
  `kontak` VARCHAR(255) NOT NULL,
  `work` VARCHAR(255) NOT NULL,
  `deist` VARCHAR(255) NULL DEFAULT NULL,
  `prim` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`vendingmachine`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`vendingmachine` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `location` VARCHAR(255) NOT NULL,
  `model` VARCHAR(255) NOT NULL,
  `type_machine` VARCHAR(255) NOT NULL,
  `status` VARCHAR(255) NOT NULL,
  `installation_date` DATE NOT NULL,
  `last_service_date` DATE NOT NULL,
  `total_income` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`maintenance`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`maintenance` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `vending_machine_id` INT NOT NULL,
  `maintenance_date` DATE NOT NULL,
  `work_description` VARCHAR(255) NOT NULL,
  `problems` VARCHAR(255) NOT NULL,
  `executor` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `maintenance_vending_machine_id` (`vending_machine_id` ASC) VISIBLE,
  CONSTRAINT `maintenance_ibfk_1`
    FOREIGN KEY (`vending_machine_id`)
    REFERENCES `franprof`.`vendingmachine` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`modem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`modem` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `model` VARCHAR(255) NOT NULL,
  `wifi` VARCHAR(255) NOT NULL,
  `iter` VARCHAR(255) NOT NULL,
  `strana` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`monitor_ta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`monitor_ta` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `connection_status` VARCHAR(255) NOT NULL,
  `last_connection` INT NOT NULL,
  `load_percent` INT NOT NULL,
  `money_amount` INT NOT NULL,
  `events` VARCHAR(255) NOT NULL,
  `location` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`new_table`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`new_table` (
  `Lox` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Lox`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`news`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`news` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `date` VARCHAR(255) NOT NULL,
  `text` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`otchet_kompanyu`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`otchet_kompanyu` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `itigo_kompanu` VARCHAR(255) NOT NULL,
  `deqist` VARCHAR(255) NOT NULL,
  `sotrud` VARCHAR(255) NOT NULL,
  `naluch_avtom` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`otchet_monitor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`otchet_monitor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `itogo_avtomatov` VARCHAR(255) NOT NULL,
  `rabotaut` VARCHAR(255) NOT NULL,
  `repairs_are_pending` VARCHAR(255) NOT NULL,
  `uroven_sred` VARCHAR(255) NOT NULL,
  `ob_verch` VARCHAR(255) NOT NULL,
  `zamenu` VARCHAR(255) NOT NULL,
  `new_oborud` VARCHAR(255) NOT NULL,
  `monitor` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`otchet_torgov_avtomat`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`otchet_torgov_avtomat` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `itigo_avtomatov` INT NOT NULL,
  `uspolzuen` VARCHAR(255) NOT NULL,
  `svobodno` VARCHAR(255) NOT NULL,
  `rabotaet` VARCHAR(255) NOT NULL,
  `ne_rabotaey` VARCHAR(255) NOT NULL,
  `trebue_obsluch` VARCHAR(255) NOT NULL,
  `provetka` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`product` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `price` INT NOT NULL,
  `quantity_in_stock` INT NOT NULL,
  `minimum_stock` INT NOT NULL,
  `sales_trend` FLOAT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`profile_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`profile_user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `tg` VARCHAR(255) NULL DEFAULT NULL,
  `vk` VARCHAR(255) NULL DEFAULT NULL,
  `github` VARCHAR(255) NULL DEFAULT NULL,
  `web` VARCHAR(255) NULL DEFAULT NULL,
  `full_name` VARCHAR(255) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `phone` VARCHAR(255) NULL DEFAULT NULL,
  `adress` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `profile_user_user_id` (`user_id` ASC) VISIBLE,
  CONSTRAINT `profile_user_ibfk_1`
    FOREIGN KEY (`user_id`)
    REFERENCES `franprof`.`autorizregus` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`sale`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`sale` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `vending_machine_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  `total_amount` INT NOT NULL,
  `sale_datetime` DATETIME NOT NULL,
  `payment_method` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `sale_vending_machine_id` (`vending_machine_id` ASC) VISIBLE,
  INDEX `sale_product_id` (`product_id` ASC) VISIBLE,
  CONSTRAINT `sale_ibfk_1`
    FOREIGN KEY (`vending_machine_id`)
    REFERENCES `franprof`.`vendingmachine` (`id`),
  CONSTRAINT `sale_ibfk_2`
    FOREIGN KEY (`product_id`)
    REFERENCES `franprof`.`product` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`soston_svz`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`soston_svz` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comp` VARCHAR(255) NOT NULL,
  `pay` VARCHAR(255) NOT NULL,
  `time` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`svodka`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`svodka` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `price` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`torfavt`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`torfavt` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `model` VARCHAR(255) NOT NULL,
  `kompany` VARCHAR(255) NOT NULL,
  `modem` VARCHAR(255) NOT NULL,
  `adress` VARCHAR(255) NOT NULL,
  `word` VARCHAR(255) NOT NULL,
  `deist` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 12
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`torgavt`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`torgavt` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `last_connection` INT NOT NULL,
  `load_percent` INT NOT NULL,
  `money_amount` INT NOT NULL,
  `events` VARCHAR(255) NULL DEFAULT NULL,
  `address` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `phone` VARCHAR(255) NOT NULL,
  `role` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `franprof`.`zagrux`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `franprof`.`zagrux` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `base` VARCHAR(255) NOT NULL,
  `minim` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb3;

USE `musuem` ;

-- -----------------------------------------------------
-- Table `musuem`.`authorization`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `musuem`.`authorization` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `login` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `musuem`.`authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `musuem`.`authors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `birth_date` VARCHAR(255) NOT NULL,
  `death_date` VARCHAR(255) NOT NULL,
  `country` VARCHAR(255) NOT NULL,
  `biography` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 16
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `musuem`.`exposition`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `musuem`.`exposition` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `start_date` VARCHAR(255) NOT NULL,
  `end_date` VARCHAR(255) NOT NULL,
  `location` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `musuem`.`exhibit`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `musuem`.`exhibit` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `creation_year` INT NOT NULL,
  `material` VARCHAR(255) NOT NULL,
  `dimensions` VARCHAR(255) NOT NULL,
  `value` INT NOT NULL,
  `condition` VARCHAR(255) NOT NULL,
  `exposishi` VARCHAR(255) NULL DEFAULT NULL,
  `image` VARCHAR(255) NULL DEFAULT NULL,
  `aftor_id` INT NULL DEFAULT NULL,
  `exposition_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `aftor` (`aftor_id` ASC) VISIBLE,
  INDEX `Exput_id_idx` (`exposition_id` ASC) VISIBLE,
  CONSTRAINT `exhibit_ibfk_1`
    FOREIGN KEY (`aftor_id`)
    REFERENCES `musuem`.`authors` (`id`),
  CONSTRAINT `Exput_id`
    FOREIGN KEY (`exposition_id`)
    REFERENCES `musuem`.`exposition` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `musuem`.`role`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `musuem`.`role` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_user_id` INT NOT NULL,
  `role` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `role_id_user_id` (`id_user_id` ASC) VISIBLE,
  CONSTRAINT `role_ibfk_1`
    FOREIGN KEY (`id_user_id`)
    REFERENCES `musuem`.`authorization` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
