CREATE TABLE `cn360` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `number` varchar(30) NOT NULL,
 `tag` varchar(100) NOT NULL,
 `address` varchar(200) NOT NULL,
 PRIMARY KEY (`id`),
 UNIQUE KEY `number` (`number`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8