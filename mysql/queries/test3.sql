-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema testing_here
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema testing_here
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `testing_here` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `testing_here`.`test_table`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `testing_here`.`test_table` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mydb`.`test2`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`test2` (
  `id` INT NOT NULL,
  `potato` VARCHAR(45) NULL,
  `test_table_id` VARCHAR(45) NULL,
  `test_table_id1` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_test2_test_table_idx` (`test_table_id1` ASC) VISIBLE,
  CONSTRAINT `fk_test2_test_table`
    FOREIGN KEY (`test_table_id1`)
    REFERENCES `testing_here`.`test_table` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `testing_here` ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
