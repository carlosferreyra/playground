package com.github.carlosferreyra.examples;

import java.util.List;
import java.util.Optional;
import java.util.logging.Logger;
import java.util.stream.Collectors;

/**
 * Example demonstrating modern Java features
 */
public class ModernJavaExample {
    private static final Logger logger = Logger.getLogger(ModernJavaExample.class.getName());

    // Example of a record (Java 16+)
    public record Person(String name, int age) {}

    public List<String> processNames(List<String> names) {
        return names.stream()
            .filter(name -> !name.isEmpty())
            .map(String::toUpperCase)
            .collect(Collectors.toList());
    }

    public Optional<Person> findPerson(List<Person> people, String name) {
        return people.stream()
            .filter(person -> person.name().equals(name))
            .findFirst();
    }
}