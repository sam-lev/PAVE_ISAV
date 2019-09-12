class PAVE
{
public:
    using type = vtkm::Float32;
    using visualisation = vtkm::cont::ArrayHandle<type>
    void open(std::string &file);
    void save(visualisation &v);
    void visualize(vtkm::rendering::Canvas &canvas); 
};
