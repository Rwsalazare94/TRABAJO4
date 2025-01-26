import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;

public class VentanaPrincipal extends JFrame implements ActionListener {
    // Clases internas y atributos
    static class Persona {
        String nombre;
        String apellidos;
        String teléfono;
        String dirección;

        public Persona(String nombre, String apellidos, String teléfono, String dirección) {
            this.nombre = nombre;
            this.apellidos = apellidos;
            this.teléfono = teléfono;
            this.dirección = dirección;
        }
    }

    static class ListaPersonas {
        Vector<Persona> listaPersonas; // Atributo que identifica un vector de personas

        public ListaPersonas() {
            listaPersonas = new Vector<>(); // Crea el vector de personas
        }

        public void añadirPersona(Persona p) {
            listaPersonas.add(p); // Añade la persona al vector
        }

        public void eliminarPersona(int i) {
            listaPersonas.removeElementAt(i); // Elimina la persona en la posición i
        }

        public void borrarLista() {
            listaPersonas.removeAllElements(); // Elimina todas las personas
        }
    }

    // Atributos de la ventana principal
    private ListaPersonas lista;
    private Container contenedor;
    private JLabel nombre, apellidos, teléfono, dirección;
    private JTextField campoNombre, campoApellidos, campoTeléfono, campoDirección;
    private JButton añadir, eliminar, borrarLista;
    private JList<String> listaNombres;
    private DefaultListModel<String> modelo;
    private JScrollPane scrollLista;

    public VentanaPrincipal() {
        lista = new ListaPersonas();
        inicio();
        setTitle("Personas");
        setSize(270,350);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);
    }

    private void inicio() {
        contenedor = getContentPane();
        contenedor.setLayout(null);

        // Inicialización de etiquetas y campos de texto
        nombre = new JLabel("Nombre:");
        nombre.setBounds(20, 20, 135, 23);
        campoNombre = new JTextField();
        campoNombre.setBounds(105, 20, 135, 23);

        apellidos = new JLabel("Apellidos:");
        apellidos.setBounds(20, 50, 135, 23);
        campoApellidos = new JTextField();
        campoApellidos.setBounds(105, 50, 135, 23);

        teléfono = new JLabel("Teléfono:");
        teléfono.setBounds(20, 80, 135, 23);
        campoTeléfono = new JTextField();
        campoTeléfono.setBounds(105, 80, 135, 23);

        dirección = new JLabel("Dirección:");
        dirección.setBounds(20, 110, 135, 23);
        campoDirección = new JTextField();
        campoDirección.setBounds(105, 110, 135, 23);

        // Botones de acción
        añadir = new JButton("Añadir");
        añadir.setBounds(105, 150, 80, 23);
        añadir.addActionListener(this);

        eliminar = new JButton("Eliminar");
        eliminar.setBounds(20, 280, 80, 23);
        eliminar.addActionListener(this);

        borrarLista = new JButton("Borrar Lista");
        borrarLista.setBounds(120, 280, 120, 23);
        borrarLista.addActionListener(this);

        // JList para mostrar los elementos
        listaNombres = new JList<>();
        listaNombres.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        modelo = new DefaultListModel<>();
        scrollLista = new JScrollPane(listaNombres);
        scrollLista.setBounds(20, 190 ,220, 80);

        // Añadir componentes al contenedor
        contenedor.add(nombre);
        contenedor.add(campoNombre);
        contenedor.add(apellidos);
        contenedor.add(campoApellidos);
        contenedor.add(teléfono);
        contenedor.add(campoTeléfono);
        contenedor.add(dirección);
        contenedor.add(campoDirección);
        contenedor.add(añadir);
        contenedor.add(eliminar);
        contenedor.add(borrarLista);
        contenedor.add(scrollLista);
    }

    @Override
    public void actionPerformed(ActionEvent evento) {
        if (evento.getSource() == añadir) {
            añadirPersona();
        }
        if (evento.getSource() == eliminar) {
            eliminarNombre(listaNombres.getSelectedIndex());
        }
        if (evento.getSource() == borrarLista) {
            borrarLista();
        }
    }

    private void añadirPersona() {
        Persona p = new Persona(campoNombre.getText(), campoApellidos.getText(),
                                campoTeléfono.getText(), campoDirección.getText());
        lista.añadirPersona(p);
        String elemento = campoNombre.getText() + "-" + campoApellidos.getText() + "-" + campoTeléfono.getText() + "-" + campoDirección.getText();
        modelo.addElement(elemento);
        listaNombres.setModel(modelo);

        // Limpiar los campos de texto
        campoNombre.setText("");
        campoApellidos.setText("");
        campoTeléfono.setText("");
        campoDirección.setText("");
    }

    private void eliminarNombre(int indice) {
        if (indice >= 0) {
            modelo.removeElementAt(indice);
            lista.eliminarPersona(indice);
        } else {
            JOptionPane.showMessageDialog(null, "Debe seleccionar un elemento", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void borrarLista() {
        lista.borrarLista();
        modelo.clear();
    }

    public static void main(String[] args) {
        VentanaPrincipal miVentanaPrincipal = new VentanaPrincipal();
        miVentanaPrincipal.setVisible(true);
    }
}
