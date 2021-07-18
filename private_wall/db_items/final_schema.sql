-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema private_wall
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema private_wall
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `private_wall` DEFAULT CHARACTER SET utf8 ;
USE `private_wall` ;

-- -----------------------------------------------------
-- Table `private_wall`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `private_wall`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `private_wall`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `private_wall`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `message_body` TEXT NULL DEFAULT NULL,
  `recipient_id` INT NOT NULL,
  `sender_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_users_idx` (`recipient_id` ASC) VISIBLE,
  INDEX `fk_messages_users1_idx` (`sender_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_users`
    FOREIGN KEY (`recipient_id`)
    REFERENCES `private_wall`.`users` (`id`),
  CONSTRAINT `fk_messages_users1`
    FOREIGN KEY (`sender_id`)
    REFERENCES `private_wall`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
