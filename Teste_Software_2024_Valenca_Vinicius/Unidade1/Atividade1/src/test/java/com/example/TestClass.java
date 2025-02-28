package com.example;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class TestClass {

    @Test
    public void testCheckNamesThrowsExceptionForShortNames() {
        ClassToTest foo = new ClassToTest();
        List<String> names = Arrays.asList("Joe", "Al", "Sam");

        
        IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> foo.checkNames(names));
        assertEquals("O nome precisa ter pelo menos 3 letras: Al", exception.getMessage());
    }

    @Test
    public void testCheckNamesDoesNotThrowExceptionForValidNames() {
        ClassToTest foo = new ClassToTest();
        List<String> names = Arrays.asList("Joe", "Sam", "Ann");

        
        foo.checkNames(names);
    }
}