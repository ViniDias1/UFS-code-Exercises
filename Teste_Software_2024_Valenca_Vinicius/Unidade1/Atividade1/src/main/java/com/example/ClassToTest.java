package com.example;
import java.util.List;

public class ClassToTest {
    public void checkNames(List<String> names) {
        for (String name : names) {
            if (name.length() <= 2) {
                throw new IllegalArgumentException("O nome precisa ter pelo menos 3 letras: " + name);
            }
        }
    }
}