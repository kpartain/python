-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema belt_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema belt_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `belt_db` DEFAULT CHARACTER SET utf8 ;
USE `belt_db` ;

-- -----------------------------------------------------
-- Table `belt_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `belt_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(100) NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `belt_db`.`cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `belt_db`.`cars` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `price` INT NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `make` VARCHAR(45) NOT NULL,
  `year` INT NOT NULL,
  `description` MEDIUMTEXT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `seller_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cars_users_idx` (`seller_id` ASC) VISIBLE,
  CONSTRAINT `fk_cars_users`
    FOREIGN KEY (`seller_id`)
    REFERENCES `belt_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
